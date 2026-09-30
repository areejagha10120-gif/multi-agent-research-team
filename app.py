import streamlit as st

from crew import run_research


st.set_page_config(
    page_title="Research Team",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="collapsed",
)


st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background: #f7f9fc;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2.5rem;
        padding-bottom: 4rem;
    }

    /* Hide default Streamlit decoration */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* Hero */
    .hero {
        background: linear-gradient(
            135deg,
            #0f172a 0%,
            #172554 100%
        );
        border-radius: 24px;
        padding: 42px;
        margin-bottom: 28px;
        color: white;
        box-shadow: 0 20px 50px rgba(15, 23, 42, 0.12);
    }

    .eyebrow {
        font-size: 13px;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: #93c5fd;
        margin-bottom: 12px;
    }

    .hero-title {
        font-size: 42px;
        line-height: 1.1;
        font-weight: 750;
        margin: 0;
        letter-spacing: -0.03em;
    }

    .hero-subtitle {
        font-size: 17px;
        color: #cbd5e1;
        margin-top: 14px;
        max-width: 680px;
        line-height: 1.6;
    }

    /* Cards */
    .card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 24px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.05);
        margin-bottom: 18px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 5px;
    }

    .card-description {
        font-size: 14px;
        color: #64748b;
        margin-bottom: 18px;
    }

    /* Agent status */
    .agent {
        display: flex;
        align-items: center;
        padding: 14px 16px;
        border-radius: 13px;
        margin-bottom: 8px;
        background: #f8fafc;
        border: 1px solid #edf0f4;
    }

    .agent.active {
        background: #eff6ff;
        border-color: #bfdbfe;
    }

    .agent.complete {
        background: #f0fdf4;
        border-color: #bbf7d0;
    }

    .agent-dot {
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: #cbd5e1;
        margin-right: 12px;
    }

    .agent.active .agent-dot {
        background: #2563eb;
        box-shadow: 0 0 0 5px #dbeafe;
    }

    .agent.complete .agent-dot {
        background: #16a34a;
    }

    .agent-name {
        font-size: 14px;
        font-weight: 650;
        color: #1e293b;
    }

    .agent-status {
        margin-left: auto;
        font-size: 12px;
        color: #64748b;
    }

    /* Report */
    .report {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 20px;
        padding: 34px;
        box-shadow: 0 8px 30px rgba(15, 23, 42, 0.05);
    }

    /* Input */
    textarea {
        border-radius: 14px !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-weight: 700;
        border: none;
        background: #2563eb;
        color: white;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: #1d4ed8;
        transform: translateY(-1px);
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# HERO
# ---------------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="eyebrow">AI Research Workspace</div>
        <div class="hero-title">
            Research deeper.<br>
            Verify before you trust.
        </div>
        <div class="hero-subtitle">
            A multi-agent research team that plans investigations,
            searches the web, verifies claims, analyzes sources,
            and produces a structured report.
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# INPUT
# ---------------------------------------------------------

st.markdown(
    """
    <div class="card">
        <div class="card-title">What would you like to research?</div>
        <div class="card-description">
            Ask a question that requires multiple sources and evidence.
        </div>
    """,
    unsafe_allow_html=True,
)

question = st.text_area(
    "Research question",
    placeholder=(
        "Example: What are the major applications of AI agents "
        "in healthcare, and what evidence exists for their benefits?"
    ),
    height=120,
    label_visibility="collapsed",
)

start = st.button("Start Research")

st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# AGENT STATUS
# ---------------------------------------------------------

if "research_started" not in st.session_state:
    st.session_state.research_started = False


if start:

    if not question.strip():
        st.warning("Please enter a research question.")
        st.stop()

    st.session_state.research_started = True

    st.markdown(
        """
        <div class="card">
            <div class="card-title">Research Team</div>
            <div class="card-description">
                Five specialized agents are working through your question.
            </div>
        """,
        unsafe_allow_html=True,
    )

    statuses = [
        ("Research Planner", "active"),
        ("Web Researcher", "waiting"),
        ("Fact Checker", "waiting"),
        ("Source Analyst", "waiting"),
        ("Research Synthesizer", "waiting"),
    ]

    status_placeholder = st.empty()

    def render_agents(active_index):
        html = ""

        names = [
            "Research Planner",
            "Web Researcher",
            "Fact Checker",
            "Source Analyst",
            "Research Synthesizer",
        ]

        for index, name in enumerate(names):

            if index < active_index:
                state = "complete"
                status = "Complete"
            elif index == active_index:
                state = "active"
                status = "Working now"
            else:
                state = ""
                status = "Waiting"

            html += f"""
            <div class="agent {state}">
                <div class="agent-dot"></div>
                <div class="agent-name">{name}</div>
                <div class="agent-status">{status}</div>
            </div>
            """

        return html

    # Initial status
    status_placeholder.markdown(
        render_agents(0),
        unsafe_allow_html=True,
    )

    try:

        # CrewAI runs the actual workflow.
        # The visible stages provide a clean user-facing
        # progress experience.
        result = run_research(question)

        status_placeholder.markdown(
            render_agents(5),
            unsafe_allow_html=True,
        )

        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown(
            """
            <div class="report">
                <div class="card-title">Research Report</div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(str(result))

        st.markdown("</div>", unsafe_allow_html=True)

    except Exception as e:

        st.markdown("</div>", unsafe_allow_html=True)

        st.error(
            f"Research could not be completed. Details: {str(e)}"
        )
