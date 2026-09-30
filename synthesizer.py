from crewai import Agent
from llm import get_llm


def create_synthesizer():
    return Agent(
        role="Research Report Synthesizer",
        goal=(
            "Transform the verified research into a clear, "
            "well-structured and evidence-based report."
        ),
        backstory=(
            "You are an expert research writer. "
            "You combine verified findings without inventing information. "
            "You clearly separate established facts, uncertainty, "
            "and conflicting evidence."
        ),
        llm=get_llm(),
        allow_delegation=False,
        verbose=False,
    )
