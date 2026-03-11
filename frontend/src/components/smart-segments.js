import Chart from "chart.js/auto";
import { createSectionHeader } from "./section-header.js";

export function renderSmartSegments(data, container) {
  const { axes, segments } = data;

  container.innerHTML = `
    ${createSectionHeader(4, "Smart Segmentation", "AI-discovered behavioral clusters across your subscriber base", "Act 2 \u2014 Here\u2019s What AI Sees")}
    <div class="segment-layout">
      <div>
        <div class="radar-chart-wrap"><canvas id="chart-radar"></canvas></div>
      </div>
      <div class="segment-cards">
        ${segments.map((seg) => `
          <div class="segment-card" style="border-left-color:${seg.color}">
            <div class="segment-card-name" style="color:${seg.color}">${seg.name}</div>
            <div class="segment-card-desc">${seg.description}</div>
            <div class="segment-card-stats">
              <span><strong>${seg.size}</strong> subscribers</span>
              <span>Avg eng: <strong>${seg.avg_engagement}</strong></span>
              <span>Avg tenure: <strong>${seg.avg_tenure_months}mo</strong></span>
            </div>
          </div>
        `).join("")}
      </div>
    </div>
  `;

  new Chart(document.getElementById("chart-radar"), {
    type: "radar",
    data: {
      labels: axes,
      datasets: segments.map((seg) => ({
        label: seg.name,
        data: seg.radar_values,
        borderColor: seg.color,
        backgroundColor: seg.color + "1a",
        borderWidth: 2,
        pointRadius: 3,
        pointBackgroundColor: seg.color,
      })),
    },
    options: {
      responsive: true,
      maintainAspectRatio: true,
      scales: {
        r: {
          beginAtZero: true,
          max: 100,
          ticks: { stepSize: 20, font: { size: 10 }, backdropColor: "transparent" },
          pointLabels: { font: { size: 11 } },
          grid: { color: "#e2e8f0" },
          angleLines: { color: "#e2e8f0" },
        },
      },
      plugins: {
        legend: { position: "bottom", labels: { usePointStyle: true, pointStyleWidth: 8, font: { size: 11 }, padding: 12 } },
      },
    },
  });
}
