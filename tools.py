from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from ddgs import DDGS


class WebSearchInput(BaseModel):
    query: str = Field(
        ...,
        description="The web search query to investigate."
    )


class WebSearchTool(BaseTool):
    name: str = "Web Search"
    description: str = (
        "Search the live web for current information. "
        "Use this to find reliable sources, facts, dates, "
        "reports, statistics, and supporting evidence."
    )
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        try:
            results = DDGS().text(
                query,
                max_results=8
            )

            if not results:
                return "No search results were found."

            formatted = []

            for i, result in enumerate(results, start=1):
                title = result.get("title", "Untitled")
                url = result.get("href", "")
                body = result.get("body", "")

                formatted.append(
                    f"RESULT {i}\n"
                    f"Title: {title}\n"
                    f"URL: {url}\n"
                    f"Summary: {body}\n"
                )

            return "\n".join(formatted)

        except Exception as e:
            return f"Web search failed: {str(e)}"
