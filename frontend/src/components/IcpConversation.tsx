import { useState } from "react";
import { useMutation, useQueryClient } from "@tanstack/react-query";
import { createIcpConversation } from "../lib/api";
import type { ConversationResponse } from "../types/api.types";

interface Props {
  onCreated: (response: ConversationResponse) => void;
  onCancel: () => void;
}

export default function IcpConversation({ onCreated, onCancel }: Props) {
  const [message, setMessage] = useState("");
  const queryClient = useQueryClient();

  const mutation = useMutation({
    mutationFn: createIcpConversation,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ["icp-models"] });
      onCreated(data);
    },
  });

  return (
    <div className="space-y-4">
      <div>
        <label className="block text-sm font-semibold text-gray-900 mb-1">
          Describe your ideal customer
        </label>
        <p className="text-xs text-muted mb-2">
          Tell Claude about your target market — industry, company size, job titles,
          pain points, tech stack, or anything relevant. Claude will extract a
          structured ICP from your description.
        </p>
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="e.g. We sell dev tools to mid-market SaaS companies (100-500 employees). Our buyers are VPs of Engineering or CTOs who care about developer productivity..."
          rows={5}
          className="w-full px-3 py-2 border border-gray-200 rounded-sm text-sm resize-y focus:outline-none focus:border-primary"
        />
      </div>

      {mutation.isError && (
        <div className="text-danger text-sm">
          Failed: {mutation.error.message}
        </div>
      )}

      <div className="flex gap-3">
        <button
          onClick={() => mutation.mutate(message)}
          disabled={!message.trim() || mutation.isPending}
          className="py-2 px-5 rounded-sm text-sm font-semibold bg-primary text-white transition-opacity hover:opacity-85 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {mutation.isPending ? "Claude is thinking..." : "Generate ICP"}
        </button>
        <button
          onClick={onCancel}
          disabled={mutation.isPending}
          className="py-2 px-5 rounded-sm text-sm font-semibold text-muted hover:text-gray-700 transition-colors"
        >
          Cancel
        </button>
      </div>
    </div>
  );
}
