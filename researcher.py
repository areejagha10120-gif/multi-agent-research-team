from crewai import Agent
from llm import get_llm
from tools import WebSearchTool


def create_researcher():
    return Agent(
        role="Web Research Specialist",
        goal=(
            "Find relevant, recent, and trustworthy information "
            "from multiple web sources."
        ),
        backstory=(
            "You are a meticulous web researcher. "
            "You search broadly, compare sources, and collect "
            "specific evidence rather than relying on assumptions."
        ),
        llm=get_llm(),
        tools=[WebSearchTool()],
        allow_delegation=False,
        verbose=False,
    )
