import streamlit as st


def load_css():
    st.markdown("""
    <style>

    /* -----------------------------
       Main App
    ------------------------------*/

    .main {
        background-color: #F7F9FC;
        padding-top: 1rem;
    }

    /* Hide Streamlit default menu */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    /* -----------------------------
       Hero Title
    ------------------------------*/

    .hero-title{
        font-size:48px;
        font-weight:800;
        color:#1f4e79;
        margin-bottom:5px;
    }

    .hero-subtitle{
        font-size:20px;
        color:#555;
        margin-bottom:25px;
    }

    /* -----------------------------
       Cards
    ------------------------------*/

    .metric-card{

        background:white;

        padding:18px;

        border-radius:16px;

        box-shadow:0px 3px 12px rgba(0,0,0,.08);

        text-align:center;

        margin-bottom:10px;

    }

    /* -----------------------------
       Pipeline
    ------------------------------*/

    .pipeline-card{

        background:white;

        padding:20px;

        border-radius:16px;

        box-shadow:0px 3px 12px rgba(0,0,0,.08);

    }

    /* -----------------------------
       Newsletter
    ------------------------------*/

    .newsletter{

        background:white;

        padding:25px;

        border-radius:16px;

        box-shadow:0px 3px 12px rgba(0,0,0,.08);

    }

    /* -----------------------------
       Buttons
    ------------------------------*/

    .stButton>button{

        width:100%;

        height:60px;

        border-radius:15px;

        font-size:22px;

        font-weight:700;

        background:#1f77b4;

        color:white;

        border:none;

    }

    .stButton>button:hover{

        background:#135d9e;

        color:white;

    }

    /* -----------------------------
       Download Buttons
    ------------------------------*/

    .stDownloadButton>button{

        width:100%;

        height:50px;

        border-radius:12px;

    }

    </style>
    """, unsafe_allow_html=True)