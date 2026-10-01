import os
import streamlit as st
from crewai import LLM


def get_llm():
    """
    Create the OpenAI LLM used by all CrewAI agents.
    """

    try:
        api_key = st.secrets.get("OPENAI_API_KEY")
    except Exception:
        api_key = None

    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OPENAI_API_KEY is missing. "
            "Add your OpenAI API key to Streamlit Secrets."
        )

    return LLM(
        model="openai/gpt-5.6-luna",
        api_key=api_key,
        temperature=0.2,
    )
