import os
import streamlit as st
from crewai import LLM


def get_llm():
    """
    Create the Gemini LLM used by all CrewAI agents.
    """

    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add your Google AI Studio API key to Streamlit Secrets."
        )

    return LLM(
        model="gemini/gemini-3.8-flash",
        api_key=api_key,
    )
