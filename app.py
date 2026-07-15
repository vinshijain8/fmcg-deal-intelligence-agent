import streamlit as st

from src.styles import load_css

from src.ui import (
    show_header,
    show_kpis,
    show_newsletter_tab,
    show_analytics_tab,
    show_raw_data_tab,
    show_downloads,
)

from src.fetch_news import fetch_news
from src.clean import clean_news
from src.relevance import filter_relevant_news
from src.deduplicate import deduplicate_news
from src.credibility import score_news
from src.newsletter import generate_newsletter
from src.exporter import export_files


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="FMCG Deal Intelligence Agent",
    page_icon="📰",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.image("assets/logo.png", width=170)

    st.markdown("## FMCG Intelligence")

    st.caption(
        "AI Powered M&A Monitoring Dashboard"
    )

    st.divider()

    st.success("📰 NewsAPI Connected")

    st.success("🤖 Gemini Connected")

    st.success("✅ Pipeline Ready")

    st.divider()

    st.markdown("### Pipeline")

    st.write("1️⃣ Fetch News")

    st.write("2️⃣ Clean Data")

    st.write("3️⃣ Relevance Filter")

    st.write("4️⃣ Deduplicate")

    st.write("5️⃣ Credibility Score")

    st.write("6️⃣ AI Newsletter")

    st.divider()

    st.info(
        "Click **Generate Newsletter** to run the complete pipeline."
    )


# ==========================================================
# HEADER
# ==========================================================

show_header()

show_kpis()


# ==========================================================
# GENERATE SECTION
# ==========================================================

newsletter = None

with st.container(border=True):

    st.subheader("🚀 Generate Latest Newsletter")

    st.write(
        """
Fetch the latest FMCG acquisition, merger and investment news,
clean the data, score credibility and generate a professional
business newsletter using Gemini AI.
"""
    )

    generate = st.button(
        "Generate Newsletter",
        use_container_width=True,
        type="primary"
    )


# ==========================================================
# RUN PIPELINE
# ==========================================================

if generate:

    progress = st.progress(0)

    status = st.empty()

    status.info("📰 Fetching latest news...")
    fetch_news()
    progress.progress(15)

    status.info("🧹 Cleaning news...")
    clean_news()
    progress.progress(30)

    status.info("🎯 Filtering FMCG deal news...")
    filter_relevant_news()
    progress.progress(50)

    status.info("🔁 Removing duplicate articles...")
    deduplicate_news()
    progress.progress(65)

    status.info("⭐ Scoring credibility...")
    score_news()
    progress.progress(80)

    status.info("🤖 Generating newsletter...")
    newsletter = generate_newsletter()
    progress.progress(95)

    status.info("📄 Exporting files...")
    export_files()
    progress.progress(100)

    status.success("✅ Newsletter Generated Successfully!")

    st.balloons()


# ==========================================================
# TABS
# ==========================================================

tab1, tab2, tab3 = st.tabs(
    [
        "📰 Newsletter",
        "📊 Analytics",
        "📂 Raw Data"
    ]
)


# ==========================================================
# NEWSLETTER TAB
# ==========================================================

with tab1:

    with st.container(border=True):

        if newsletter:

            show_newsletter_tab(newsletter)

        else:

            st.info(
                "Generate a newsletter to view AI-generated results."
            )


# ==========================================================
# ANALYTICS TAB
# ==========================================================

with tab2:

    with st.container(border=True):

        show_analytics_tab()


# ==========================================================
# RAW DATA TAB
# ==========================================================

with tab3:

    with st.container(border=True):

        show_raw_data_tab()


# ==========================================================
# DOWNLOADS
# ==========================================================

with st.container(border=True):

    show_downloads()


# ==========================================================
# FOOTER
# ==========================================================

st.divider()

st.caption(
    "© 2026 FMCG Deal Intelligence Agent | "
    "Built with Streamlit • NewsAPI • Gemini AI • Pandas • RapidFuzz"
)