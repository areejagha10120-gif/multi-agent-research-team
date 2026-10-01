import os
import streamlit as st
from crewai import LLM


def get_llm():
    """
    Create the Claude LLM used by all CrewAI agents.
    """

    try:
        api_key = st.secrets.get("ANTHROPIC_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise ValueError(
            "ANTHROPIC_API_KEY is missing. "
            "Add your Anthropic API key to Streamlit Secrets."
        )

    return LLM(
        model="anthropic/claude-sonnet-4-5",
        api_key=api_key,
        temperature=0.2,
    )
