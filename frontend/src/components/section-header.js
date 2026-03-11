/**
 * Creates a numbered section header with act label.
 * @param {number} number - Section number (1-7)
 * @param {string} title - Section title
 * @param {string} subtitle - Brief description
 * @param {string} actLabel - Narrative act label
 * @returns {string} HTML string
 */
export function createSectionHeader(number, title, subtitle, actLabel) {
  return `
    <div class="section-header">
      <span class="section-number">${number}</span>
      <div class="section-header-text">
        <span class="section-act">${actLabel}</span>
        <h2 class="section-title">${title}</h2>
        <p class="section-subtitle">${subtitle}</p>
      </div>
    </div>
  `;
}
