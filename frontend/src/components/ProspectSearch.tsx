import { useState, useEffect } from "react";
import { useQuery, useMutation } from "@tanstack/react-query";
import { fetchIcpModels, searchProspects, listProspects } from "../lib/api";
import type { ProspectResult } from "../types/api.types";
import Card from "./Card";
import ProspectTable from "./ProspectTable";

interface Props {
  initialModelId?: string | null;
}

export default function ProspectSearch({ initialModelId }: Props) {
  const [selectedModel, setSelectedModel] = useState<string>("");
  const [results, setResults] = useState<ProspectResult | null>(null);
  const [statusMsg, setStatusMsg] = useState<{ type: string; text: string } | null>(null);

  const { data: models } = useQuery({
    queryKey: ["icp-models"],
    queryFn: fetchIcpModels,
  });

  // Pick effective model: explicit selection > initialModelId > active model > first
  const activeModel = models?.find((m) => m.is_active);
  const effectiveModel =
    selectedModel ||
    initialModelId ||
    activeModel?.id ||
    models?.[0]?.id ||
    "";

  // When initialModelId changes (e.g. from "Search Prospects" button), sync it
  useEffect(() => {
    if (initialModelId) setSelectedModel(initialModelId);
  }, [initialModelId]);

  const searchMutation = useMutation({
    mutationFn: async () => searchProspects(effectiveModel),
    onSuccess: (data) => {
      setStatusMsg({ type: "success", text: `Found ${data.total} prospects` });
      setResults(data);
    },
    onError: (err: Error) => {
      setStatusMsg({ type: "error", text: `Search failed: ${err.message}` });
      setResults(null);
    },
  });

  const loadMutation = useMutation({
    mutationFn: async () => listProspects(effectiveModel),
    onSuccess: (data) => {
      if (data.total === 0) {
        setStatusMsg({ type: "muted", text: 'No saved prospects. Click "Search Prospects" first.' });
      } else {
        setStatusMsg({ type: "success", text: `${data.total} saved prospects` });
      }
      setResults(data);
    },
    onError: (err: Error) => {
      setStatusMsg({ type: "error", text: `Load failed: ${err.message}` });
      setResults(null);
    },
  });

  const statusColors: Record<string, string> = {
    success: "text-success font-semibold",
    error: "text-danger",
    muted: "text-muted",
  };

  return (
    <Card>
      <h2 className="text-lg font-bold text-gray-900 mb-4">Prospect Search</h2>

      <div className="flex items-end gap-3 mb-4 flex-wrap">
        <div className="flex flex-col gap-1 flex-1 min-w-[200px]">
          <label className="text-[0.7rem] font-semibold uppercase tracking-wide text-muted">
            ICP Model
          </label>
          <select
            value={effectiveModel}
            onChange={(e) => setSelectedModel(e.target.value)}
            disabled={!models || models.length === 0}
            className="py-2 px-3 border border-gray-200 rounded-sm text-sm bg-white text-gray-900 cursor-pointer"
          >
            {!models ? (
              <option>Loading models…</option>
            ) : models.length === 0 ? (
              <option>No ICP models — create one first</option>
            ) : (
              models.map((m) => (
                <option key={m.id} value={m.id}>
                  {m.name}
                  {m.is_active ? " (active)" : ""}
                </option>
              ))
            )}
          </select>
        </div>

        <button
          onClick={() => searchMutation.mutate()}
          disabled={!effectiveModel || searchMutation.isPending}
          className="py-2 px-5 rounded-sm text-[0.82rem] font-semibold bg-primary text-white whitespace-nowrap transition-opacity hover:opacity-85 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {searchMutation.isPending ? "Searching…" : "Search Prospects"}
        </button>

        <button
          onClick={() => loadMutation.mutate()}
          disabled={!effectiveModel || loadMutation.isPending}
          className="py-2 px-5 rounded-sm text-[0.82rem] font-semibold bg-dark text-gray-300 whitespace-nowrap transition-opacity hover:opacity-85 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loadMutation.isPending ? "Loading…" : "Load Saved"}
        </button>
      </div>

      {(searchMutation.isPending || loadMutation.isPending) && (
        <div className="text-accent text-[0.82rem] mb-3">
          {searchMutation.isPending
            ? "Searching Apollo for matching contacts…"
            : "Loading saved prospects…"}
        </div>
      )}

      {statusMsg && !searchMutation.isPending && !loadMutation.isPending && (
        <div className={`text-[0.82rem] mb-3 ${statusColors[statusMsg.type] ?? ""}`}>
          {statusMsg.text}
        </div>
      )}

      {results && <ProspectTable prospects={results.items} />}
    </Card>
  );
}
