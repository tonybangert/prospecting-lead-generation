export default function BriefDisplay({ brief }) {
  const { profile, news, summary, talking_points, icebreakers } = brief;

  return (
    <div className="mt-8 space-y-6">
      {/* Profile Header */}
      <div className="bg-white rounded-lg shadow p-6">
        <h2 className="text-2xl font-bold text-gray-900">{profile.full_name}</h2>
        <p className="text-gray-600">{profile.headline}</p>
        <div className="mt-2 flex flex-wrap gap-2 text-sm text-gray-500">
          {profile.company && <span className="bg-gray-100 px-2 py-1 rounded">{profile.company}</span>}
          {profile.industry && <span className="bg-gray-100 px-2 py-1 rounded">{profile.industry}</span>}
          {profile.location && <span className="bg-gray-100 px-2 py-1 rounded">{profile.location}</span>}
        </div>
      </div>

      {/* Summary */}
      {summary && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-2">Summary</h3>
          <p className="text-gray-700 leading-relaxed">{summary}</p>
        </div>
      )}

      {/* Talking Points */}
      {talking_points.length > 0 && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-3">Talking Points</h3>
          <ul className="space-y-2">
            {talking_points.map((point, i) => (
              <li key={i} className="flex gap-2 text-gray-700">
                <span className="text-blue-500 font-bold shrink-0">&bull;</span>
                {point}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Icebreakers */}
      {icebreakers.length > 0 && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-3">Icebreakers</h3>
          <div className="space-y-3">
            {icebreakers.map((msg, i) => (
              <div key={i} className="bg-blue-50 border border-blue-100 rounded-lg p-4 text-gray-700">
                {msg}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Recent News */}
      {news.length > 0 && (
        <div className="bg-white rounded-lg shadow p-6">
          <h3 className="text-lg font-semibold text-gray-900 mb-3">Recent Company News</h3>
          <div className="space-y-3">
            {news.map((article, i) => (
              <a
                key={i}
                href={article.url}
                target="_blank"
                rel="noopener noreferrer"
                className="block p-3 border border-gray-200 rounded-lg hover:bg-gray-50 transition-colors"
              >
                <p className="font-medium text-gray-900">{article.title}</p>
                <p className="text-sm text-gray-500 mt-1">{article.source} &middot; {article.published_at?.slice(0, 10)}</p>
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
