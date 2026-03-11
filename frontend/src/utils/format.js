const currencyFmt = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  maximumFractionDigits: 0,
});

const currencyDetailFmt = new Intl.NumberFormat("en-US", {
  style: "currency",
  currency: "USD",
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});

const compactFmt = new Intl.NumberFormat("en-US", {
  notation: "compact",
  maximumFractionDigits: 1,
});

export function formatCurrency(value) {
  return currencyFmt.format(value);
}

export function formatCurrencyDetail(value) {
  return currencyDetailFmt.format(value);
}

export function formatPercent(value) {
  return `${value.toFixed(1)}%`;
}

export function formatCompact(value) {
  return compactFmt.format(value);
}

export function formatNumber(value) {
  return value.toLocaleString("en-US");
}
