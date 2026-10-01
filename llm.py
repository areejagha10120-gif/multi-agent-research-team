import os
import streamlit as st
from crewai import LLM


def get_llm():
    """
    Create the Gemini LLM used by all CrewAI agents.

    The API key is read from Streamlit Secrets first,
    then from the environment.
    """

    # Try Streamlit Cloud Secrets
    try:
        api_key = st.secrets.get("GEMINI_API_KEY")
    except Exception:
        api_key = None

    # Fall back to environment variable
    if not api_key:
        api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY is missing. "
            "Add your Google AI Studio API key to Streamlit Secrets."
        )

    return LLM(
        model="gemini/gemini-2.5-flash",
        api_key=api_key,
        temperature=0.2,
    )
