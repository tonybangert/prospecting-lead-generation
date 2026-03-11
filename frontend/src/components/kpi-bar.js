import { createSectionHeader } from "./section-header.js";
import { formatCurrency, formatPercent, formatNumber } from "../utils/format.js";

// Simulated deltas for the demo (positive = good, context-dependent)
const DELTAS = [
  { delta: "+3.2%", dir: "up" },      // MRR
  { delta: "+4", dir: "up" },          // Total Subscribers
  { delta: "+1.5%", dir: "up" },       // Active Rate
  { delta: "+$0.42", dir: "up" },      // ARPU
  { delta: "-0.8", dir: "down" },      // Avg Engagement
  { delta: "-2.1%", dir: "up" },       // Churn Rate (down is good, shown as green)
];

export function renderKpiBar(data, container) {
  const metrics = [
    { value: formatCurrency(data.mrr), label: "Monthly Recurring Revenue" },
    { value: formatNumber(data.total_subscribers), label: "Total Subscribers" },
    { value: formatPercent(data.active_rate), label: "Active Rate" },
    { value: formatCurrency(data.arpu), label: "Avg Revenue / User" },
    { value: data.avg_engagement.toFixed(0), label: "Avg Engagement Score" },
    { value: formatPercent(data.churn_rate), label: "Churn Rate" },
  ];

  const arrow = (dir) => dir === "up" ? "\u25B2" : "\u25BC";

  container.innerHTML = `
    ${createSectionHeader(1, "Key Performance Metrics", "Real-time subscription health at a glance", "Act 1 \u2014 Here\u2019s What You Have")}
    <div class="kpi-grid">
      ${metrics.map((m, i) => `
        <div class="kpi-card">
          <div class="kpi-value">${m.value}</div>
          <div class="kpi-delta ${DELTAS[i].dir}">${arrow(DELTAS[i].dir)} ${DELTAS[i].delta}</div>
          <div class="kpi-label">${m.label}</div>
        </div>
      `).join("")}
    </div>
  `;
}
