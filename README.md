# AI Equity Research Agent

An AI-powered research assistant that converts a collection of company documents into a concise, source-backed equity research brief for retail investors.

## Features

* Accepts an NSE ticker and company research documents.
* Extracts text from PDF, DOCX, Markdown, TXT, CSV, and XLSX files.
* Uses an LLM to summarize company performance, growth drivers, risks, and open questions.
* Generates a Markdown report with five sections: Snapshot, Bull Case, Bear Case, Open Questions, and Sources.
* Provides a Streamlit interface and a Markdown download option.
* Flags conflicting claims rather than automatically choosing one.

## Technology Stack

* Python
* Streamlit
* Agno
* Groq API
* Model: `openai/gpt-oss-120b`
* pypdf, python-docx, and openpyxl for document extraction

## Project Structure

```text
AI_AGENT/
├── app.py
├── research_agent.py
├── document_reader.py
├── system_prompt.md
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── tests/
    └── test_log.md
```

## Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_AGENT
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Obtain an API key from https://console.groq.com/keys.

Never commit `.env` or publish API keys.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Assignment Test Case

The test case uses the supplied research documents for Sarvottam Cables Ltd (NSE: SRVCABLE), with the assignment's specified analysis date of 23 September 2026.

Upload the eight documents through the application and generate the brief.

## Design Decisions

* **Document-only research:** The agent uses supplied documents rather than searching for external company information.
* **Explicit source IDs:** Documents are labeled so the generated brief can refer to supporting evidence.
* **Conflict handling:** Conflicting financial figures should be reported as unresolved unless the supplied evidence establishes which is correct.
* **Separate system prompt:** Keeping instructions in `system_prompt.md` makes prompt changes easy to review and test.
* **Prompt iteration:** Three runs document changes to conflict handling, conciseness, and evidence auditing.

## Limitations

* Generated claims and citations require manual verification against the original documents.
* Scanned PDFs without extractable text may require OCR.
* Large research packs may be truncated by the current implementation.
* The model may miss context, misinterpret financial figures, or produce unsupported conclusions.
* The application is a research aid, not investment advice.
* API availability, model access, and rate limits depend on the Groq account.

## Testing

See [`tests/test_log.md`](tests/test_log.md) for the three-run prompt-iteration log.

## Security

Keep `.env` and API keys private. Use `.env.example` as a template without real credentials.
