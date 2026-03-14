import type { Prospect } from "../types/api.types";

interface Props {
  prospects: Prospect[];
}

function scoreClass(score: number | null): string {
  if (score == null) return "bg-bg text-text-light";
  if (score >= 0.7) return "bg-success-bg text-success";
  if (score >= 0.4) return "bg-warning-bg text-warning";
  return "bg-danger-bg text-danger";
}

function fmtScore(score: number | null): string {
  if (score == null) return "N/A";
  return `${Math.round(score * 100)}%`;
}

// TODO(human): Implement renderScoreBreakdown
// This function receives a score_breakdown object like:
//   { firmographic_fit: 0.85, tech_fit: 0.6, persona_match: 0.9, timing_signals: 0.3, data_confidence: 0.7 }
// It should return JSX that visualizes each dimension in a compact, scannable way.
// Return null if breakdown is null.
function renderScoreBreakdown(
  _breakdown: Record<string, number> | null,
): React.ReactNode {
  // TODO(human): Replace this placeholder — see instructions above
  return null;
}

export default function ProspectTable({ prospects }: Props) {
  if (prospects.length === 0) {
    return <p className="text-muted text-center py-8">No prospects to display.</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="w-full border-collapse text-[0.8rem]">
        <thead>
          <tr>
            {["Name", "Title", "Company", "Location", "Seniority", "Email", "ICP Fit", "Breakdown", "Profile"].map(
              (h) => (
                <th
                  key={h}
                  className="text-left font-semibold text-muted py-2 px-3 border-b-2 border-dark uppercase text-[0.68rem] tracking-wide"
                >
                  {h}
                </th>
              ),
            )}
          </tr>
        </thead>
        <tbody>
          {prospects.map((p) => (
            <tr key={p.id} className="hover:bg-bg">
              <td className="py-2 px-3 border-b border-gray-200 font-semibold whitespace-nowrap">
                {p.first_name ?? ""} {p.last_name ?? ""}
              </td>
              <td className="py-2 px-3 border-b border-gray-200">{p.title ?? "—"}</td>
              <td className="py-2 px-3 border-b border-gray-200">{p.company_name ?? "—"}</td>
              <td className="py-2 px-3 border-b border-gray-200">{p.company_location ?? "—"}</td>
              <td className="py-2 px-3 border-b border-gray-200 capitalize">{p.seniority ?? "—"}</td>
              <td className="py-2 px-3 border-b border-gray-200">
                {p.email ? (
                  <a href={`mailto:${p.email}`} className="text-primary hover:underline">
                    {p.email}
                  </a>
                ) : "—"}
              </td>
              <td className="py-2 px-3 border-b border-gray-200">
                <span
                  className={`inline-block px-2 py-0.5 rounded-[3px] text-[0.72rem] font-bold font-mono ${scoreClass(p.icp_fit_score)}`}
                >
                  {fmtScore(p.icp_fit_score)}
                </span>
              </td>
              <td className="py-2 px-3 border-b border-gray-200">
                {renderScoreBreakdown(p.score_breakdown)}
              </td>
              <td className="py-2 px-3 border-b border-gray-200">
                {p.linkedin_url ? (
                  <a
                    href={p.linkedin_url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary no-underline font-medium hover:underline"
                  >
                    LinkedIn
                  </a>
                ) : "—"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
