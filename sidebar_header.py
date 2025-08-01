import streamlit as st

def render_sidebar_header():
    st.markdown("""
        <style>
        [data-testid="stSidebarNav"]::before {
            content: "Francis 林高天 — Following the Pulse of Regeneration 跟随再生的脉动";
            white-space: pre-wrap;
            display: block;
            font-weight: bold;
            font-size: 1.1rem;
            padding: 20px 16px 10px 16px;
            color: #2E7D32; /* Ecology green */
        }
        </style>
    """, unsafe_allow_html=True)