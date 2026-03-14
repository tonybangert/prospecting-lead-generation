import { useState } from "react";
import Header from "./components/Header";
import TabBar from "./components/TabBar";
import IcpModelList from "./components/IcpModelList";
import ProspectSearch from "./components/ProspectSearch";
import Footer from "./components/Footer";

const TABS = [
  { key: "models", label: "ICP Models" },
  { key: "prospects", label: "Prospects" },
];

export default function App() {
  const [activeTab, setActiveTab] = useState("models");
  const [prospectModelId, setProspectModelId] = useState<string | null>(null);

  function handleSearchProspects(modelId: string) {
    setProspectModelId(modelId);
    setActiveTab("prospects");
  }

  return (
    <>
      <Header />
      <main className="mx-auto max-w-container flex flex-col gap-5 p-6">
        <TabBar tabs={TABS} active={activeTab} onSelect={setActiveTab} />
        {activeTab === "models" && (
          <IcpModelList onSearchProspects={handleSearchProspects} />
        )}
        {activeTab === "prospects" && (
          <ProspectSearch initialModelId={prospectModelId} />
        )}
      </main>
      <Footer />
    </>
  );
}
