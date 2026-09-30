from crewai import Agent
from llm import get_llm
from tools import WebSearchTool


def create_source_analyst():
    return Agent(
        role="Source Analysis Specialist",
        goal=(
            "Analyze the quality, relevance, recency, and "
            "independence of sources used in the research."
        ),
        backstory=(
            "You are a source-evaluation specialist. "
            "You distinguish primary sources from secondary reporting "
            "and identify weak, outdated, duplicated, or unsupported evidence."
        ),
        llm=get_llm(),
        tools=[WebSearchTool()],
        allow_delegation=False,
        verbose=False,
    )
