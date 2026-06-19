import streamlit as st
import os
from pathlib import Path

st.set_page_config(
    page_title="JARVIS Dashboard",
    layout="wide",
    page_icon="\ud83e\udde0"
)

st.title("\ud83e\udde0 JARVIS Dashboard")
st.caption("JARVIS Agent v1.0 — Hardened • Zero Trust • Runtime Capability Enforcement")

# Sidebar navigation
page = st.sidebar.radio(
    "Navigation",
    [
        "\ud83d\udcd8 Knowledge Base",
        "\ud83d\udd27 Skills",
        "\ud83e\uddea Tests & Verification",
        "\ud83c\udfa4 Voice Setup",
        "\ud83d\udcca System Status"
    ],
    index=0
)

KB_PATH = Path("/app/knowledge-base")

if page == "\ud83d\udcd8 Knowledge Base":
    st.header("\ud83d\udcd8 Knowledge Base")

    if not KB_PATH.exists():
        st.error("knowledge-base directory not found inside the container.")
    else:
        md_files = sorted([f.name for f in KB_PATH.glob("*.md")])

        if not md_files:
            st.warning("No Markdown documents found in knowledge-base/")
        else:
            col1, col2 = st.columns([1, 3])

            with col1:
                st.metric("Documents Available", len(md_files))
                selected_file = st.selectbox(
                    "Select document to view",
                    md_files,
                    index=0,
                    help="Choose a document from the knowledge base"
                )

            with col2:
                if selected_file:
                    file_path = KB_PATH / selected_file
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            content = f.read()

                        st.subheader(selected_file)
                        st.markdown(content, unsafe_allow_html=False)

                        st.download_button(
                            label="\ud83d\udcbe Download this document",
                            data=content,
                            file_name=selected_file,
                            mime="text/markdown"
                        )
                    except Exception as e:
                        st.error(f"Could not read file: {e}")

elif page == "\ud83d\udd27 Skills":
    st.header("\ud83d\udd27 Available Skills")
    st.info("Skill modules and execution buttons will be added in the next iteration.")
    st.write("Planned: Adversarial OSINT, Multimedia Analysis, Runtime Enforcement, and more.")

elif page == "\ud83e\uddea Tests & Verification":
    st.header("\ud83e\uddea Tests & Verification")
    if st.button("Run Basic System Check", type="primary"):
        st.success("System check placeholder — real verification logic will be wired here.")
    st.caption("This will eventually execute container health checks, knowledge-base integrity, and capability tests.")

elif page == "\ud83c\udfa4 Voice Setup":
    st.header("\ud83c\udfa4 Voice Interaction Setup")
    st.info("Voice interaction controls and configuration will be integrated here.")

elif page == "\ud83d\udcca System Status":
    st.header("\ud83d\udcca System Status")
    st.success("JARVIS v1.0 is running successfully inside Docker with full port exposure.")
    st.write(f"**Working directory:** {os.getcwd()}")
    st.write(f"**Python version:** {os.sys.version.split()[0]}")
    st.caption("More live metrics (container health, loaded modules, resource usage) will be added next.")

st.sidebar.markdown("---")
st.sidebar.caption("JARVIS Professional Agent Environment | Docker + Streamlit")
