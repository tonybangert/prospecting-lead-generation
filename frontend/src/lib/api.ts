import type {
  IcpModel,
  ConversationResponse,
  ProspectResult,
} from "../types/api.types";

const BASE = "/api";

async function fetchJSON<T>(path: string): Promise<T> {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) throw new Error(`API ${path}: ${res.status}`);
  return res.json() as Promise<T>;
}

async function postJSON<T>(path: string, body: unknown): Promise<T> {
  const res = await fetch(`${BASE}${path}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`API ${path}: ${res.status}`);
  return res.json() as Promise<T>;
}

/* ── ICP endpoints ─────────────────────────────────────── */
export const fetchIcpModels = () => fetchJSON<IcpModel[]>("/icp/");

export const fetchIcpModel = (id: string) => fetchJSON<IcpModel>(`/icp/${id}`);

export const activateIcpModel = (id: string) =>
  postJSON<IcpModel>(`/icp/${id}/activate`, {});

export const createIcpConversation = (message: string) =>
  postJSON<ConversationResponse>("/icp/conversation", { message });

/* ── Prospect endpoints ────────────────────────────────── */
export async function searchProspects(
  modelId: string,
  page = 1,
  perPage = 25,
): Promise<ProspectResult> {
  return postJSON(`/prospects/search/${modelId}`, { page, per_page: perPage });
}

export const listProspects = (modelId: string, page = 1, perPage = 25) =>
  fetchJSON<ProspectResult>(`/prospects/${modelId}?page=${page}&per_page=${perPage}`);
