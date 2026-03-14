import type { Config } from "tailwindcss";

export default {
  content: ["./index.html", "./src/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        primary: { DEFAULT: "#db2777", light: "#ec4899", bg: "#fdf2f8" },
        secondary: { DEFAULT: "#7c3aed", bg: "#f5f3ff" },
        accent: { DEFAULT: "#f59e0b", bg: "#fffbeb" },
        success: { DEFAULT: "#10b981", bg: "#ecfdf5" },
        warning: { DEFAULT: "#f59e0b", bg: "#fffbeb" },
        danger: { DEFAULT: "#ef4444", bg: "#fef2f2" },
        cyan: { DEFAULT: "#06b6d4", bg: "#ecfeff" },
        dark: { DEFAULT: "#0f0f1a", surface: "#1a1a2e", border: "#2d2d44" },
        surface: "#ffffff",
        bg: "#fafafa",
        muted: "#6b7280",
        "text-light": "#9ca3af",
        ticker: { green: "#22c55e", red: "#ef4444" },
        status: {
          active: "#10b981",
          churned: "#ef4444",
          paused: "#f59e0b",
          trial: "#7c3aed",
        },
        risk: { low: "#10b981", medium: "#f59e0b", high: "#ef4444" },
      },
      fontFamily: {
        mono: [
          "SF Mono",
          "Cascadia Code",
          "Fira Code",
          "Consolas",
          "Courier New",
          "monospace",
        ],
      },
      borderRadius: {
        DEFAULT: "10px",
        sm: "6px",
      },
      boxShadow: {
        DEFAULT:
          "0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04)",
        md: "0 4px 6px rgba(0,0,0,0.06), 0 2px 4px rgba(0,0,0,0.03)",
      },
      maxWidth: {
        container: "1400px",
      },
      keyframes: {
        "ticker-scroll": {
          "0%": { transform: "translateX(0)" },
          "100%": { transform: "translateX(-50%)" },
        },
      },
      animation: {
        "ticker-scroll": "ticker-scroll 30s linear infinite",
      },
    },
  },
  plugins: [],
} satisfies Config;
