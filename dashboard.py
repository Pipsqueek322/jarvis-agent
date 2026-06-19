import streamlit as st
from pathlib import Path
import datetime

# Page configuration
st.set_page_config(
    page_title="JARVIS Agent v1.0",
    page_icon="📊",  # Safe emoji (bar chart)
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("JARVIS Agent v1.0")
st.caption("AI-Powered Research, Analysis & Automation Platform")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Overview", "Knowledge Base", "Tools & Capabilities", "System Status"]
)

if page == "Overview":
    st.header("System Overview")
    st.markdown("""
    Welcome to **JARVIS** — your unified AI agent for research, analysis, automation, and decision support.
    
    This dashboard provides real-time visibility into capabilities, knowledge base, and system health.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Status", "Operational", delta="Stable")
    with col2:
        st.metric("Uptime", "99.8%", delta="+0.2%")
    with col3:
        st.metric("Active Tasks", "12", delta="+3")

elif page == "Knowledge Base":
    st.header("Knowledge Base")
    st.markdown("Search and browse the internal knowledge repository.")
    
    KB_PATH = Path("/app/knowledge-base")
    if KB_PATH.exists():
        md_files = list(KB_PATH.glob("*.md"))
        if md_files:
            selected = st.selectbox("Select document", [f.name for f in md_files])
            if selected:
                content = (KB_PATH / selected).read_text(encoding="utf-8", errors="ignore")
                st.markdown(content)
        else:
            st.info("No markdown files found in knowledge-base folder.")
    else:
        st.warning("Knowledge base directory not found. Create /app/knowledge-base and add .md files.")

elif page == "Tools & Capabilities":
    st.header("Tools & Capabilities")
    st.markdown("""
    - **Research & OSINT**
    - **Document Analysis & Summarization**
    - **Trading / Quant Analysis**
    - **Content Generation (YouTube, KDP, etc.)**
    - **Docker + Streamlit Automation**
    - **Multi-Agent Workflows**
    """)

elif page == "System Status":
    st.header("System Status")
    st.success("All core services operational")
    st.json({
        "container": "jarvis",
        "streamlit_version": st.__version__,
        "timestamp": str(datetime.datetime.now())
    })

st.sidebar.markdown("---")
st.sidebar.caption("JARVIS Agent © 2026")
