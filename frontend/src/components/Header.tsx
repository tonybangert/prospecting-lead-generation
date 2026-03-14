export default function Header() {
  return (
    <header className="bg-dark text-white py-5 px-6 border-b-[3px] border-accent">
      <div className="mx-auto max-w-container flex items-center justify-between">
        <div className="flex items-center gap-3">
          <h1 className="text-xl font-bold tracking-tight">PerformanceLabs</h1>
          <span className="bg-accent text-dark text-[0.65rem] font-bold px-2.5 py-1 rounded-[3px] uppercase tracking-wide">
            Prospecting
          </span>
        </div>
        <p className="text-text-light text-sm text-right">ICP-Driven Prospect Research</p>
      </div>
    </header>
  );
}
