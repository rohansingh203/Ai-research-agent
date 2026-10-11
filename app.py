
import os
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

from document_reader import (
    SUPPORTED_EXTENSIONS,
    read_research_pack,
)
from research_agent import generate_research_brief

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

st.set_page_config(
    page_title="AI Equity Research Agent",
    page_icon="📊",
    layout="wide",
)

st.title("AI Equity Research Agent")
st.write(
    "Turn a company's research documents into a concise, "
    "source-backed brief for a retail investor."
)

with st.sidebar:
    st.header("Research settings")
    ticker = st.text_input(
        "NSE ticker",
        value="SRVCABLE",
    ).strip().upper()

    st.caption("Assignment reference date: 23 September 2026")
    st.info(
        "This agent analyzes uploaded documents only. "
        "It does not independently verify company information."
    )

st.subheader("1. Upload research documents")

uploaded_files = st.file_uploader(
    "Select the eight research-pack documents",
    type=[ext.lstrip(".") for ext in SUPPORTED_EXTENSIONS],
    accept_multiple_files=True,
)

if uploaded_files:
    st.write(f"Uploaded files: {len(uploaded_files)}")

    with st.expander("Review filenames"):
        for file in uploaded_files:
            st.write(f"- {file.name}")

if len(uploaded_files or []) != 8:
    st.warning(
        "The required test case contains eight documents. "
        "Upload all eight for the assignment test."
    )

st.subheader("2. Generate the brief")

if not os.getenv("GROQ_API_KEY"):
    st.error(
        "GROQ_API_KEY is missing. Add your key to .env "
        "and restart the application."
    )

can_generate = (
    bool(ticker)
    and bool(uploaded_files)
    and bool(os.getenv("GROQ_API_KEY"))
)

if st.button(
    "Generate Research Brief",
    type="primary",
    disabled=not can_generate,
):
    try:
        with st.spinner("Reading sources and analyzing evidence..."):
            documents = read_research_pack(uploaded_files)

            if not documents:
                raise ValueError(
                    "No supported documents were found."
                )

            brief = generate_research_brief(ticker, documents)

        st.session_state["brief"] = brief
        st.session_state["ticker"] = ticker
        st.session_state["sources"] = [
            doc["filename"] for doc in documents
        ]

    except Exception as exc:
        st.error("The brief could not be generated.")
        st.caption(
            "Check the API key, model availability, network, "
            "and document formats."
        )
        with st.expander("Technical error details"):
            st.code(str(exc))

if st.session_state.get("brief"):
    brief = st.session_state["brief"]
    report_ticker = st.session_state.get("ticker", ticker)

    st.divider()
    st.subheader(f"Research Brief: {report_ticker}")
    st.markdown(brief)

    st.download_button(
        "Download Markdown brief",
        data=brief,
        file_name=f"{report_ticker.lower()}_research_brief.md",
        mime="text/markdown",
    )

    with st.expander("Documents processed"):
        for filename in st.session_state.get("sources", []):
            st.write(f"- {filename}")

    st.caption(
        "Verify citations against the original documents "
        "before relying on the report."
    )