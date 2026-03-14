interface Tab {
  key: string;
  label: string;
}

interface Props {
  tabs: Tab[];
  active: string;
  onSelect: (key: string) => void;
}

export default function TabBar({ tabs, active, onSelect }: Props) {
  return (
    <nav className="flex gap-1 border-b border-gray-200 mb-6">
      {tabs.map((tab) => (
        <button
          key={tab.key}
          onClick={() => onSelect(tab.key)}
          className={`px-5 py-2.5 text-sm font-semibold border-b-2 transition-colors -mb-px ${
            active === tab.key
              ? "border-primary text-primary"
              : "border-transparent text-muted hover:text-gray-700 hover:border-gray-300"
          }`}
        >
          {tab.label}
        </button>
      ))}
    </nav>
  );
}
