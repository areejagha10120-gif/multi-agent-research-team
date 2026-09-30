from crewai import Agent
from llm import get_llm
from tools import WebSearchTool


def create_fact_checker():
    return Agent(
        role="Fact Verification Specialist",
        goal=(
            "Independently verify important claims using "
            "reliable external sources."
        ),
        backstory=(
            "You are a skeptical fact checker. "
            "You do not automatically trust research findings. "
            "You search for supporting and contradictory evidence "
            "and clearly identify uncertainty."
        ),
        llm=get_llm(),
        tools=[WebSearchTool()],
        allow_delegation=False,
        verbose=False,
    )
