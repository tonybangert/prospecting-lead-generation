import Chart from "chart.js/auto";
import { createSectionHeader } from "./section-header.js";

const RISK_COLORS = { low: "#059669", medium: "#d97706", high: "#dc2626" };

export function renderChurnPrediction(data, container) {
  const { scatter_data, risk_distribution, high_risk_subscribers } = data;

  container.innerHTML = `
    ${createSectionHeader(3, "Churn Prediction", "AI-powered risk scoring across the subscriber base", "Act 2 \u2014 Here\u2019s What AI Sees")}
    <div class="risk-cards">
      <div class="risk-card low">
        <div class="risk-card-value">${risk_distribution.low}</div>
        <div class="risk-card-label">Low Risk</div>
      </div>
      <div class="risk-card medium">
        <div class="risk-card-value">${risk_distribution.medium}</div>
        <div class="risk-card-label">Medium Risk</div>
      </div>
      <div class="risk-card high">
        <div class="risk-card-value">${risk_distribution.high}</div>
        <div class="risk-card-label">High Risk</div>
      </div>
    </div>
    <div class="scatter-layout" style="margin-top:1.5rem;">
      <div>
        <div class="scatter-chart-wrap"><canvas id="chart-scatter"></canvas></div>
      </div>
      <div class="risk-sidebar">
        <h3 style="font-size:0.9rem;font-weight:600;margin-bottom:0.5rem;">Highest Risk Subscribers</h3>
        <ul class="high-risk-list">
          ${high_risk_subscribers.map((s) => `
            <li class="high-risk-item">
              <span class="hr-score">${(s.risk_score * 100).toFixed(0)}%</span>
              <span class="hr-name">${s.name}</span>
              <span class="hr-factors">${s.contributing_factors[0]}</span>
            </li>
          `).join("")}
        </ul>
      </div>
    </div>
  `;

  const grouped = { low: [], medium: [], high: [] };
  scatter_data.forEach((p) => {
    grouped[p.risk_level].push({ x: p.engagement_score, y: p.risk_score * 100 });
  });

  new Chart(document.getElementById("chart-scatter"), {
    type: "scatter",
    data: {
      datasets: Object.entries(grouped).map(([level, points]) => ({
        label: `${level.charAt(0).toUpperCase() + level.slice(1)} Risk`,
        data: points,
        backgroundColor: RISK_COLORS[level] + "99",
        borderColor: RISK_COLORS[level],
        borderWidth: 1.5,
        pointRadius: 5,
        pointHoverRadius: 7,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        x: { title: { display: true, text: "Engagement Score", font: { size: 12 } }, min: 0, max: 100 },
        y: { title: { display: true, text: "Churn Risk %", font: { size: 12 } }, min: 0, max: 100 },
      },
      plugins: {
        legend: { position: "top", labels: { usePointStyle: true, pointStyleWidth: 8, font: { size: 11 } } },
        tooltip: {
          callbacks: {
            label: (ctx) => `Engagement: ${ctx.parsed.x}, Risk: ${ctx.parsed.y.toFixed(0)}%`,
          },
        },
      },
    },
  });
}
