import os

# CrewAI workaround for Groq cache_breakpoint issue
try:
    import crewai.llms.cache as crew_cache
    crew_cache.mark_cache_breakpoint = lambda message: message
except Exception:
    pass

from crewai import LLM


def get_llm():
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. "
            "Add it in Streamlit Cloud Secrets."
        )

    return LLM(
        model="openai/gpt-oss-120b",
        base_url="https://api.groq.com/openai/v1",
        api_key=api_key,
        temperature=0.2,
    )
