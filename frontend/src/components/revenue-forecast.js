import Chart from "chart.js/auto";
import { createSectionHeader } from "./section-header.js";
import { formatCurrency, formatPercent } from "../utils/format.js";

export function renderRevenueForecast(data, container) {
  const { historical, projected_baseline, projected_ai_enhanced, current_mrr, baseline_projected_mrr, ai_projected_mrr, ai_uplift_pct } = data;

  container.innerHTML = `
    ${createSectionHeader(6, "Revenue Forecast", "Baseline vs AI-enhanced MRR projections \u2014 real-time, MRR growth insight", "Act 3 \u2014 Here\u2019s What AI Does")}
    <div class="forecast-layout">
      <div class="forecast-chart-wrap"><canvas id="chart-forecast"></canvas></div>
      <div class="forecast-summary">
        <div class="forecast-stat">
          <div class="forecast-stat-value">${formatCurrency(current_mrr)}</div>
          <div class="forecast-stat-label">Current MRR</div>
        </div>
        <div class="forecast-stat">
          <div class="forecast-stat-value">${formatCurrency(baseline_projected_mrr)}</div>
          <div class="forecast-stat-label">Baseline Projected</div>
        </div>
        <div class="forecast-stat">
          <div class="forecast-stat-value highlight">${formatCurrency(ai_projected_mrr)}</div>
          <div class="forecast-stat-label">AI-Enhanced Projected</div>
        </div>
        <div class="forecast-stat">
          <div class="forecast-stat-value primary">+${formatPercent(ai_uplift_pct)}</div>
          <div class="forecast-stat-label">AI Uplift</div>
        </div>
      </div>
    </div>
  `;

  const histLabels = historical.map((d) => d.month);
  const histValues = historical.map((d) => d.mrr);
  const baseLabels = projected_baseline.map((d) => d.month);
  const baseValues = projected_baseline.map((d) => d.mrr);
  const aiValues = projected_ai_enhanced.map((d) => d.mrr);

  const allLabels = [...histLabels, ...baseLabels];
  const historicalLine = [...histValues, ...Array(baseLabels.length).fill(null)];
  const baselineLine = [...Array(histLabels.length - 1).fill(null), histValues[histValues.length - 1], ...baseValues];
  const aiLine = [...Array(histLabels.length - 1).fill(null), histValues[histValues.length - 1], ...aiValues];

  new Chart(document.getElementById("chart-forecast"), {
    type: "line",
    data: {
      labels: allLabels,
      datasets: [
        {
          label: "Historical MRR",
          data: historicalLine,
          borderColor: "#7c3aed",
          backgroundColor: "#7c3aed",
          borderWidth: 2.5,
          pointRadius: 2,
          tension: 0.3,
        },
        {
          label: "Baseline Projection",
          data: baselineLine,
          borderColor: "#9ca3af",
          backgroundColor: "#9ca3af",
          borderWidth: 2,
          borderDash: [6, 3],
          pointRadius: 2,
          tension: 0.3,
        },
        {
          label: "AI-Enhanced Projection",
          data: aiLine,
          borderColor: "#22c55e",
          backgroundColor: "#22c55e" + "1a",
          borderWidth: 2.5,
          pointRadius: 2,
          tension: 0.3,
          fill: "+1",
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      interaction: { mode: "index", intersect: false },
      scales: {
        x: { grid: { display: false }, ticks: { font: { size: 10 }, maxRotation: 45 } },
        y: {
          title: { display: true, text: "MRR ($)", font: { size: 12 } },
          ticks: { callback: (v) => "$" + (v / 1000).toFixed(0) + "k" },
          grid: { color: "#f1f5f9" },
        },
      },
      plugins: {
        legend: { position: "top", labels: { usePointStyle: true, pointStyleWidth: 8, font: { size: 11 }, padding: 16 } },
        tooltip: {
          callbacks: {
            label: (ctx) => `${ctx.dataset.label}: $${ctx.parsed.y.toLocaleString()}`,
          },
        },
      },
    },
  });
}
