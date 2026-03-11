import { formatCurrency, formatPercent } from "../utils/format.js";

/**
 * Renders a scrolling stock-ticker strip with key subscription metrics.
 * Content is duplicated so the CSS animation loops seamlessly.
 */
export function renderTicker(kpis, container) {
  const items = [
    { label: "MRR", value: formatCurrency(kpis.mrr), delta: "+3.2%", dir: "up" },
    { label: "Subscribers", value: kpis.total_subscribers, delta: "+4", dir: "up" },
    { label: "Active Rate", value: formatPercent(kpis.active_rate), delta: "+1.5%", dir: "up" },
    { label: "ARPU", value: formatCurrency(kpis.arpu), delta: "+$0.42", dir: "up" },
    { label: "Engagement", value: kpis.avg_engagement.toFixed(1), delta: "-0.8", dir: "down" },
    { label: "Churn", value: formatPercent(kpis.churn_rate), delta: "-2.1%", dir: "up" },
    { label: "MRR", value: formatCurrency(kpis.mrr), delta: "+3.2%", dir: "up" },
    { label: "Subscribers", value: kpis.total_subscribers, delta: "+4", dir: "up" },
    { label: "Active Rate", value: formatPercent(kpis.active_rate), delta: "+1.5%", dir: "up" },
    { label: "ARPU", value: formatCurrency(kpis.arpu), delta: "+$0.42", dir: "up" },
    { label: "Engagement", value: kpis.avg_engagement.toFixed(1), delta: "-0.8", dir: "down" },
    { label: "Churn", value: formatPercent(kpis.churn_rate), delta: "-2.1%", dir: "up" },
  ];

  const arrow = (dir) => dir === "up" ? "\u25B2" : "\u25BC";

  const html = items.map((i) => `
    <span class="ticker-item">
      <span class="ticker-label">${i.label}</span>
      <span class="ticker-val">${i.value}</span>
      <span class="ticker-delta ${i.dir}">${arrow(i.dir)} ${i.delta}</span>
    </span>
  `).join("");

  // Duplicate content for seamless loop
  container.innerHTML = `<div class="ticker-track">${html}${html}</div>`;
}
