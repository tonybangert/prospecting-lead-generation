import Chart from "chart.js/auto";
import { createSectionHeader } from "./section-header.js";
import { formatCurrencyDetail } from "../utils/format.js";

const STATUS_COLORS = {
  active: "#10b981",
  churned: "#ef4444",
  paused: "#f59e0b",
  trial: "#7c3aed",
};

const TIER_COLORS = {
  "Free": "#9ca3af",
  "Stock Advisor": "#3b82f6",
  "Rule Breakers": "#db2777",
  "Epic": "#7c3aed",
  "Epic Plus": "#f59e0b",
  "Fool One": "#10b981",
};

function createDoughnut(canvas, labels, values, colors) {
  return new Chart(canvas, {
    type: "doughnut",
    data: {
      labels,
      datasets: [{
        data: values,
        backgroundColor: colors,
        borderWidth: 2,
        borderColor: "#ffffff",
      }],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      cutout: "60%",
      plugins: {
        legend: { position: "bottom", labels: { padding: 12, usePointStyle: true, pointStyleWidth: 8, font: { size: 11 } } },
      },
    },
  });
}

export function renderSubscriberOverview(data, container) {
  const statusLabels = Object.keys(data.status_distribution);
  const statusValues = Object.values(data.status_distribution);
  const statusColors = statusLabels.map((l) => STATUS_COLORS[l] || "#94a3b8");

  const tierLabels = Object.keys(data.tier_distribution);
  const tierValues = Object.values(data.tier_distribution);
  const tierColors = tierLabels.map((l) => TIER_COLORS[l] || "#94a3b8");

  container.innerHTML = `
    ${createSectionHeader(2, "Subscriber Overview", "Status distribution, tier breakdown, and subscriber snapshot", "Act 1 \u2014 Here\u2019s What You Have")}
    <div class="doughnut-grid">
      <div class="chart-box">
        <h3>Subscriber Status</h3>
        <div class="chart-canvas-wrap"><canvas id="chart-status"></canvas></div>
      </div>
      <div class="chart-box">
        <h3>Plan Tier Distribution</h3>
        <div class="chart-canvas-wrap"><canvas id="chart-tier"></canvas></div>
      </div>
    </div>
    <h3 style="font-size:0.9rem;font-weight:600;margin-bottom:0.75rem;">Subscriber Snapshot</h3>
    <table class="subscriber-table">
      <thead>
        <tr><th>Name</th><th>Tier</th><th>Status</th><th>Tenure</th><th>MRR</th><th>Engagement</th></tr>
      </thead>
      <tbody>
        ${data.snapshot.map((s) => `
          <tr>
            <td>${s.name}</td>
            <td>${s.plan_tier}</td>
            <td><span class="badge badge-${s.status}">${s.status}</span></td>
            <td>${s.tenure_months}mo</td>
            <td>${formatCurrencyDetail(s.monthly_rate)}</td>
            <td>${s.engagement_score}</td>
          </tr>
        `).join("")}
      </tbody>
    </table>
  `;

  createDoughnut(document.getElementById("chart-status"), statusLabels, statusValues, statusColors);
  createDoughnut(document.getElementById("chart-tier"), tierLabels, tierValues, tierColors);
}
