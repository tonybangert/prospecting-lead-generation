const BASE = "/api";

async function fetchJSON(path) {
  const res = await fetch(`${BASE}${path}`);
  if (!res.ok) throw new Error(`API ${path}: ${res.status}`);
  return res.json();
}

export const fetchKpis = () => fetchJSON("/dashboard/kpis");
export const fetchSubscribers = () => fetchJSON("/subscribers");
export const fetchChurn = () => fetchJSON("/churn");
export const fetchSegments = () => fetchJSON("/segments");
export const fetchRecommendations = () => fetchJSON("/recommendations");
export const fetchRevenueForecast = () => fetchJSON("/revenue-forecast");
export const fetchRetentionActions = () => fetchJSON("/retention-actions");
