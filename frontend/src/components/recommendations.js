import { createSectionHeader } from "./section-header.js";
import { formatCurrency } from "../utils/format.js";

export function renderRecommendations(data, container) {
  const { recommendations, total_projected_monthly_impact } = data;

  container.innerHTML = `
    ${createSectionHeader(5, "Personalized Recommendations", "AI-generated upsell and retention actions per segment", "Act 2 \u2014 Here\u2019s What AI Sees")}
    <div class="rec-summary">
      <div>
        <div class="rec-summary-value">${formatCurrency(total_projected_monthly_impact)}/mo</div>
        <div class="rec-summary-label">Total Projected Monthly Revenue Impact</div>
      </div>
    </div>
    <div class="rec-groups">
      ${recommendations.map((rec) => {
        const seg = rec.segment;
        const segColor = getSegmentColor(seg);
        return `
          <div class="rec-group">
            <div class="rec-group-header">
              <span class="rec-group-dot" style="background:${segColor}"></span>
              ${seg}
            </div>
            <div class="rec-actions">
              ${rec.actions.map((a) => `
                <div class="rec-action">
                  <div class="rec-action-type ${a.type}">${a.type}</div>
                  <div class="rec-action-title">${a.title}</div>
                  <div class="rec-action-desc">${a.description}</div>
                  <div class="rec-action-impact">
                    <strong>+${formatCurrency(a.projected_monthly_impact)}/mo</strong>
                    <span style="color:var(--text-light)">${(a.confidence * 100).toFixed(0)}% confidence</span>
                    <div class="confidence-bar">
                      <div class="confidence-bar-fill" style="width:${a.confidence * 100}%"></div>
                    </div>
                  </div>
                </div>
              `).join("")}
            </div>
          </div>
        `;
      }).join("")}
    </div>
  `;
}

function getSegmentColor(name) {
  const colors = {
    "Buy & Hold Veterans": "#db2777",
    "Casual Browsers": "#7c3aed",
    "Market Watchers": "#10b981",
    "At-Risk Disengaged": "#ef4444",
    "New Investors": "#f59e0b",
    "Price-Sensitive": "#06b6d4",
  };
  return colors[name] || "#6b7280";
}
