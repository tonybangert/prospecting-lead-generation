import type { ReactNode } from "react";

interface Props {
  title?: string;
  children: ReactNode;
  isLoading?: boolean;
  error?: string | null;
}

export default function Card({ title, children, isLoading, error }: Props) {
  if (isLoading) {
    return (
      <section className="rounded border border-gray-200 bg-white p-6 shadow text-center text-muted text-sm">
        Loading…
      </section>
    );
  }

  if (error) {
    return (
      <section className="rounded border border-gray-200 bg-white p-6 shadow">
        <div className="text-danger text-center text-sm py-8">
          Failed to load: {error}
        </div>
      </section>
    );
  }

  return (
    <section className="rounded border border-gray-200 bg-white p-6 shadow">
      {title && (
        <h2 className="text-lg font-bold text-gray-900 mb-4">{title}</h2>
      )}
      {children}
    </section>
  );
}
