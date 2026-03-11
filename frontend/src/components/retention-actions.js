import { createSectionHeader } from "./section-header.js";

const TYPE_LABELS = {
  email_campaign: "Email",
  discount_offer: "Discount",
  paywall_unlock: "Paywall",
  csm_trigger: "CSM",
  content_recommendation: "Content",
  win_back_offer: "Win-Back",
};

function formatTimestamp(ts) {
  const d = new Date(ts);
  const now = new Date();
  const diffMs = now - d;
  const diffH = Math.floor(diffMs / 3600000);
  if (diffH < 1) return "Just now";
  if (diffH < 24) return `${diffH}h ago`;
  const diffD = Math.floor(diffH / 24);
  if (diffD === 1) return "Yesterday";
  return `${diffD}d ago`;
}

export function renderRetentionActions(data, container) {
  const { actions, summary } = data;

  container.innerHTML = `
    ${createSectionHeader(7, "Automated Retention Actions", "AI agent activity log \u2014 autonomous interventions in real time", "Act 3 \u2014 Here\u2019s What AI Does")}
    <div class="timeline-summary">
      <div class="timeline-stat">
        <div class="timeline-stat-value" style="color:var(--success)">${summary.completed}</div>
        <div class="timeline-stat-label">Completed</div>
      </div>
      <div class="timeline-stat">
        <div class="timeline-stat-value" style="color:var(--warning)">${summary.in_progress}</div>
        <div class="timeline-stat-label">In Progress</div>
      </div>
      <div class="timeline-stat">
        <div class="timeline-stat-value" style="color:var(--text-light)">${summary.pending}</div>
        <div class="timeline-stat-label">Pending</div>
      </div>
    </div>
    <div class="timeline">
      ${actions.map((a) => `
        <div class="timeline-item">
          <div class="timeline-marker ${a.status}"></div>
          <div class="timeline-item-header">
            <span class="timeline-item-type">${TYPE_LABELS[a.action_type] || a.action_type}</span>
            <span class="timeline-item-name">${a.subscriber_name}</span>
            <span class="timeline-item-time">${formatTimestamp(a.timestamp)}</span>
          </div>
          <div class="timeline-item-desc">${a.description}</div>
          ${a.outcome ? `<div class="timeline-item-outcome">\u2713 ${a.outcome}</div>` : ""}
        </div>
      `).join("")}
    </div>
  `;
}
