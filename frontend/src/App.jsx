import { useState } from "react";
import ProspectForm from "./components/ProspectForm";
import BriefDisplay from "./components/BriefDisplay";

export default function App() {
  const [brief, setBrief] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async (linkedinUrl) => {
    setLoading(true);
    setError(null);
    setBrief(null);

    try {
      const response = await fetch("/api/prospect", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ linkedin_url: linkedinUrl }),
      });

      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.detail || `Request failed (${response.status})`);
      }

      const data = await response.json();
      setBrief(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-4xl mx-auto px-4 py-10">
      <header className="text-center mb-10">
        <h1 className="text-3xl font-bold text-gray-900">
          Prospect Brief Generator
        </h1>
        <p className="mt-2 text-gray-600">
          Paste a LinkedIn URL to generate a personalized sales brief
        </p>
      </header>

      <ProspectForm onSubmit={handleSubmit} loading={loading} />

      {error && (
        <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
          {error}
        </div>
      )}

      {brief && <BriefDisplay brief={brief} />}
    </div>
  );
}
