# Test Log — AI Equity Research Agent

## Project Information

* **Project:** AI Equity Research Agent
* **Test company:** Sarvottam Cables Ltd
* **NSE ticker:** SRVCABLE
* **Model:** `openai/gpt-oss-120b`
* **Inference provider:** Groq API
* **Framework:** Agno
* **User interface:** Streamlit
* **Analysis date:** 23 September 2026
* **Test input:** Eight company research documents supplied with the assignment

---

## Run 1 — Baseline Research Prompt

### Objective

Test whether the agent can generate a research brief from the supplied documents.

### Design

Used the initial system prompt instructing the model to generate five sections:

1. Snapshot
2. Bull case
3. Bear case
4. Open questions
5. Sources

The agent was instructed to use the supplied research documents and include source IDs for factual claims.

### Observed Result

The agent generated a research brief covering the company's business, financial performance, growth opportunities, risks, open questions, and source documents.

It identified conflicting Q1 FY27 revenue figures:

* ₹1,248 crore reported in the company press release.
* ₹1,428 crore reported in a news article.

### Issues Identified

* The report was longer than the intended one-page format.
* Some citations contained only source IDs without precise document locations.
* Some financial statements and interpretations needed clearer wording.
* The conflicting figures required explicit treatment as unresolved.

### Improvement Planned

Strengthen the prompt to improve conciseness, percentage interpretation, conflict handling, and separation of facts from analysis.

---

## Run 2 — Improved Conflict Handling

### Objective

Improve how the agent presents inconsistent information and financial risks.

### Design Change

Updated the system prompt with additional quality-control rules:

* Keep the report concise.
* Identify conflicting financial figures and their sources.
* Do not guess which conflicting figure is correct.
* Distinguish profit growth from profit margins.
* Separate reported facts from analytical interpretations.
* Avoid unsupported conclusions.

### Observed Result

The generated report continued to include all five required sections.

It explicitly presented both revenue figures and identified the discrepancy as unresolved. It also summarized the company's order book, capacity expansion, copper-cost pressure, receivables, and GST demand.

### Issues Identified

* The report remained lengthy.
* Most citations still identified sources without page numbers or section headings.
* The source references and financial claims still required checking against the original documents.

### Improvement Planned

Add a final evidence-audit stage to improve traceability, reduce repetition, and discourage unsupported claims.

---

## Run 3 — Final Evidence Audit

### Objective

Improve the final report's source traceability, factual discipline, and readability.

### Design Change

Added final evidence-audit instructions requiring the agent to:

* Check material financial figures against the supplied source text.
* Attach source IDs to material factual claims.
* Include page numbers or section headings when available.
* Never invent citation locations.
* Preserve unresolved discrepancies.
* Separate company-reported facts from news reports and interpretation.
* Remove repeated or irrelevant arguments.
* Keep the report suitable for a retail investor.

### Observed Result

The third report retained all five required sections and presented the two conflicting revenue figures without claiming to resolve them.

It included inline source IDs, publication dates, a source table, and an evidence-limitations note. The report was more structured and easier to scan.

### Remaining Issues

* Source URLs need to be checked against the supplied documents; example-domain URLs must not be treated as verified links.
* Page-level or section-level citations remain limited.
* Analytical statements still require verification against the source evidence.
* The report's factual accuracy has not been independently established merely by generating it.

### Future Improvements

* Add automated citation checks where feasible.
* Improve extraction of page numbers and section headings.
* Validate all references against the original documents.
* Add tests for missing evidence, conflicting figures, and unsupported claims.
* Evaluate the final report for factual accuracy and conciseness.

---

## Overall Conclusion

Across the three runs, the agent consistently generated the required research-brief structure and identified the conflicting revenue figures.

The prompt changes improved the intended handling of conflicts, evidence limitations, and concise presentation. However, the model's output still requires verification against the original research pack. Source IDs and polished writing alone do not guarantee factual accuracy.

The system is intended to assist research, not replace independent verification or provide personalized investment advice.
