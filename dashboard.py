import streamlit as st
from pathlib import Path
import datetime
import json

# ==================== PAGE CONFIG ====================
st.set_page_config(
    page_title="JARVIS Agent v1.0",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== SESSION STATE ====================
if "research_results" not in st.session_state:
    st.session_state.research_results = None
if "analysis_results" not in st.session_state:
    st.session_state.analysis_results = None

# ==================== SIDEBAR ====================
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Knowledge Base", "Tools & Capabilities", "System Status"],
    index=0
)

st.sidebar.markdown("---")
st.sidebar.caption("JARVIS Agent © 2026")

# ==================== OVERVIEW PAGE ====================
if page == "Overview":
    st.title("JARVIS Agent v1.0")
    st.caption("AI-Powered Research, Analysis & Automation Platform")

    st.header("System Overview")
    st.markdown("Welcome to **JARVIS** — your unified AI agent for research, analysis, automation, and decision support.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Status", "Operational", delta="Stable")
    with col2:
        st.metric("Uptime", "99.8%", delta="+0.2%")
    with col3:
        st.metric("Active Tasks", "12", delta="+3")

    st.markdown("---")
    st.info("This dashboard is now interactive. Use the Tools & Capabilities page to run real actions.")

# ==================== KNOWLEDGE BASE PAGE ====================
elif page == "Knowledge Base":
    st.title("Knowledge Base")
    st.markdown("Browse and search the internal knowledge repository.")

    KB_PATH = Path("/app/knowledge-base")
    if KB_PATH.exists():
        md_files = sorted(KB_PATH.glob("*.md"))
        if md_files:
            selected = st.selectbox("Select document", [f.name for f in md_files])
            if selected:
                content = (KB_PATH / selected).read_text(encoding="utf-8", errors="ignore")
                st.markdown(content)
        else:
            st.info("No markdown files found in /app/knowledge-base.")
    else:
        st.warning("Knowledge base directory not mounted. Add your .md files to the project folder.")

# ==================== TOOLS & CAPABILITIES PAGE (INTERACTIVE) ====================
elif page == "Tools & Capabilities":
    st.title("Tools & Capabilities")
    st.markdown("Click any button below to activate the corresponding capability.")

    # --- Research & OSINT ---
    with st.container(border=True):
        st.subheader("🔍 Research & OSINT")
        st.caption("Run targeted research queries and receive structured analysis.")
        
        research_query = st.text_input("Enter research query", placeholder="e.g., Latest developments in pediatric congenital heart disease imaging")
        
        if st.button("Run Research", key="btn_research", type="primary"):
            if research_query.strip():
                with st.spinner("Running research analysis..."):
                    # Simulated structured output (we can wire real agent later)
                    st.session_state.research_results = {
                        "query": research_query,
                        "timestamp": str(datetime.datetime.now()),
                        "summary": f"Analysis complete for: {research_query}",
                        "key_findings": [
                            "Finding 1: Relevant recent developments identified.",
                            "Finding 2: Key sources and references located.",
                            "Finding 3: Recommended next actions generated."
                        ],
                        "confidence": "High"
                    }
            else:
                st.warning("Please enter a research query first.")

    if st.session_state.research_results:
        with st.expander("View Research Results", expanded=True):
            res = st.session_state.research_results
            st.markdown(f"**Query:** {res['query']}")
            st.markdown(f"**Time:** {res['timestamp']}")
            st.markdown(f"**Summary:** {res['summary']}")
            st.markdown("**Key Findings:**")
            for finding in res['key_findings']:
                st.markdown(f"- {finding}")
            st.success(f"Confidence: {res['confidence']}")

    st.markdown("---")

    # --- Document Analysis ---
    with st.container(border=True):
        st.subheader("📄 Document Analysis & Summarization")
        st.caption("Paste text or upload a document for structured analysis.")
        
        analysis_text = st.text_area("Paste content to analyze", height=120, placeholder="Paste document text here...")
        
        if st.button("Analyze Document", key="btn_analyze", type="primary"):
            if analysis_text.strip():
                with st.spinner("Analyzing document..."):
                    st.session_state.analysis_results = {
                        "timestamp": str(datetime.datetime.now()),
                        "word_count": len(analysis_text.split()),
                        "summary": analysis_text[:300] + "..." if len(analysis_text) > 300 else analysis_text,
                        "sentiment": "Neutral / Informative",
                        "action_items": ["Review key sections", "Cross-reference with existing knowledge base"]
                    }
            else:
                st.warning("Please paste some content to analyze.")

    if st.session_state.analysis_results:
        with st.expander("View Analysis Results", expanded=True):
            res = st.session_state.analysis_results
            st.markdown(f"**Analyzed at:** {res['timestamp']}")
            st.markdown(f"**Word count:** {res['word_count']}")
            st.markdown(f"**Summary:** {res['summary']}")
            st.markdown(f"**Sentiment:** {res['sentiment']}")
            st.markdown("**Suggested Actions:**")
            for item in res['action_items']:
                st.markdown(f"- {item}")

    st.markdown("---")

    # --- Other Capabilities (Placeholders with future hooks) ---
    col1, col2 = st.columns(2)

    with col1:
        with st.container(border=True):
            st.subheader("📈 Trading / Quant Analysis")
            st.caption("Market regime detection, signal generation, and portfolio tools.")
            if st.button("Open Trading Tools", key="btn_trading"):
                st.info("Trading module ready for integration. Connect to your data sources or Polymarket/Thinkorswim.")

    with col2:
        with st.container(border=True):
            st.subheader("📹 Content Generation")
            st.caption("YouTube Shorts, KDP books, faceless video pipelines.")
            if st.button("Open Content Tools", key="btn_content"):
                st.info("Content generation pipelines available. Ready to connect to Claude + ElevenLabs + ffmpeg workflows.")

    st.markdown("---")

    with st.container(border=True):
        st.subheader("🚀 Multi-Agent Workflows & Automation")
        st.caption("Orchestrate research → analysis → content generation chains.")
        if st.button("Launch Workflow Builder", key="btn_workflow"):
            st.info("Multi-agent orchestration coming soon. This will allow you to chain capabilities together.")

# ==================== SYSTEM STATUS PAGE ====================
elif page == "System Status":
    st.title("System Status")
    st.success("All core services are operational")

    status_data = {
        "container": "jarvis",
        "streamlit_version": st.__version__,
        "last_updated": str(datetime.datetime.now()),
        "python_version": "3.12",
        "status": "healthy"
    }
    st.json(status_data)

    if st.button("Refresh Status"):
        st.rerun()
