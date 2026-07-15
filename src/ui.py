import streamlit as st


def show_header():

    col1, col2 = st.columns([1, 5])

    with col1:
        st.image("assets/logo.png", width=110)

    with col2:

        st.title("FMCG Deal Intelligence Agent")

        st.markdown(
            "### AI Powered M&A Monitoring Dashboard"
        )

        st.caption(
            "Generate concise FMCG deal intelligence newsletters using NewsAPI, "
            "rule-based filtering, credibility scoring and Gemini AI."
        )

    st.divider()

import pandas as pd


def show_kpis():

    try:

        raw = len(pd.read_csv("data/raw_news.csv"))

        relevant = len(pd.read_csv("data/relevant_news.csv"))

        final = len(pd.read_csv("data/scored_news.csv"))

        sources = pd.read_csv("data/scored_news.csv")["Source"].nunique()

    except Exception:

        raw = 0
        relevant = 0
        final = 0
        sources = 0

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            label="📰 Articles Fetched",
            value=raw
        )

    with c2:
        st.metric(
            label="🎯 Relevant Deals",
            value=relevant
        )

    with c3:
        st.metric(
            label="📑 Final Articles",
            value=final
        )

    with c4:
        st.metric(
            label="🌐 Sources",
            value=sources
        )

    st.divider()


def show_newsletter_tab(newsletter):

    with st.container(border=True):

        st.subheader("📰 AI Generated Newsletter")

        st.markdown(newsletter)

def show_analytics_tab():

    try:
        df = pd.read_csv("data/scored_news.csv")

    except:
        st.warning("No analytics available.")
        return

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Articles by Source")

        st.bar_chart(
            df["Source"].value_counts()
        )

    with col2:

        st.subheader("Credibility Distribution")

        st.bar_chart(
            df["Credibility"].value_counts()
        )

def show_raw_data_tab():

    try:

        df = pd.read_csv("data/scored_news.csv")

    except:

        st.warning("No processed data found.")

        return

    st.subheader("📂 Processed Articles")

    st.dataframe(
        df[
            [
                "Title",
                "Source",
                "Credibility"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )


from pathlib import Path


def show_downloads():

    st.subheader("📥 Downloads")

    c1, c2, c3, c4 = st.columns(4)

    downloads = [
        ("📄 Markdown", "output/newsletter.md", "newsletter.md", "text/markdown"),
        ("📝 Word", "output/newsletter.docx", "newsletter.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"),
        ("📦 JSON", "output/scored_news.json", "scored_news.json", "application/json"),
        ("📊 CSV", "data/scored_news.csv", "scored_news.csv", "text/csv")
    ]

    for col, (label, path, filename, mime) in zip([c1, c2, c3, c4], downloads):

        if Path(path).exists():

            with open(path, "rb") as f:

                col.download_button(
                    label,
                    data=f,
                    file_name=filename,
                    mime=mime,
                    use_container_width=True
                )                            