from crewai import Agent
from llm import get_llm
from tools import WebSearchTool


def create_planner():
    return Agent(
        role="Research Planning Specialist",
        goal=(
            "Break a research question into a clear, efficient "
            "set of research objectives."
        ),
        backstory=(
            "You are an experienced research strategist. "
            "You turn broad questions into focused research tasks "
            "and identify what evidence needs to be collected."
        ),
        llm=get_llm(),
        tools=[WebSearchTool()],
        allow_delegation=False,
        verbose=False,
    )
