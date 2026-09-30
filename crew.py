from crewai import Crew, Task, Process

from planner import create_planner
from researcher import create_researcher
from fact_checker import create_fact_checker
from source_analyst import create_source_analyst
from synthesizer import create_synthesizer


def run_research(question):

    planner = create_planner()
    researcher = create_researcher()
    fact_checker = create_fact_checker()
    source_analyst = create_source_analyst()
    synthesizer = create_synthesizer()

    planning_task = Task(
        description=f"""
        Analyze this research question:

        {question}

        Create a focused research plan.
        Identify the major questions that must be answered.
        Identify the types of evidence that should be collected.
        """,
        expected_output=(
            "A structured research plan containing the key "
            "questions and evidence requirements."
        ),
        agent=planner,
    )

    research_task = Task(
        description="""
        Using the research plan, conduct web research.

        Search multiple sources.
        Prefer authoritative and recent sources.
        Collect specific facts, evidence, dates, and URLs.

        Do not simply provide general commentary.
        """,
        expected_output=(
            "A detailed evidence collection containing claims, "
            "supporting information, and source URLs."
        ),
        agent=researcher,
        context=[planning_task],
    )

    fact_check_task = Task(
        description="""
        Independently verify the important claims found by the researcher.

        Search the web yourself.
        Look for supporting and contradictory evidence.
        Identify claims that cannot be adequately verified.

        Clearly distinguish:
        - Verified
        - Partially verified
        - Unverified
        """,
        expected_output=(
            "A fact-checking report containing the claims examined, "
            "verification status, evidence, and URLs."
        ),
        agent=fact_checker,
        context=[research_task],
    )

    source_task = Task(
        description="""
        Analyze the sources used in the research and fact checking.

        Identify:
        - Primary sources
        - Secondary sources
        - Strong supporting evidence
        - Weak or unsupported evidence
        - Outdated information
        - Conflicting sources

        Explain why particular sources are useful.
        """,
        expected_output=(
            "A source analysis describing source type, relevance, "
            "recency, and important limitations."
        ),
        agent=source_analyst,
        context=[research_task, fact_check_task],
    )

    synthesis_task = Task(
        description=f"""
        Produce the final research report for:

        {question}

        Use ONLY the research, verification, and source-analysis
        information provided by the other agents.

        Structure the report as:

        # Research Report

        ## Executive Summary

        ## Key Findings

        ## Evidence

        ## Areas of Uncertainty

        ## Source Notes

        ## Sources

        Do not invent facts or citations.
        """,
        expected_output=(
            "A polished research report with an executive summary, "
            "key findings, evidence, uncertainty, and source URLs."
        ),
        agent=synthesizer,
        context=[planning_task, research_task, fact_check_task, source_task],
    )

    crew = Crew(
        agents=[
            planner,
            researcher,
            fact_checker,
            source_analyst,
            synthesizer,
        ],
        tasks=[
            planning_task,
            research_task,
            fact_check_task,
            source_task,
            synthesis_task,
        ],
        process=Process.sequential,
        verbose=False,
    )

    result = crew.kickoff()

    return result
