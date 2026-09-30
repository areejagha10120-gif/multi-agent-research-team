from crewai import Agent
from llm import get_llm
from tools import WebSearchTool


def create_researcher():

    return Agent(
        role="Web Researcher",

        goal=(
            "Find accurate and current information from the web "
            "using the web_search tool."
        ),

        backstory=(
            "You are a careful web researcher. "
            "When you need information, use the web_search tool. "
            "When calling web_search, ALWAYS provide a 'query' argument. "
            "Never provide cursor, id, search, or other arguments. "
            "The tool call must look like: "
            "{'query': 'your search question'}."
        ),

        tools=[WebSearchTool()],

        llm=get_llm(),

        allow_delegation=False,

        verbose=False
    )
