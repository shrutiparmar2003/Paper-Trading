import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Virtual Assistant",
    page_icon="💬",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .title {
        font-size: 42px;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-top: 40px;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #4c4c4c;
        margin-bottom: 30px;
    }
    iframe {
        border: 1px solid #ccc;
        border-radius: 12px;
        display: block;
        margin: 0 auto;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #888;
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Subtitle
st.markdown('<div class="title">💬 Virtual Chat Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask your stock-related questions and get instant help from our AI assistant</div>', unsafe_allow_html=True)

# Embedded Botpress Assistant
st.markdown("""
    <iframe
        src="https://cdn.botpress.cloud/webchat/v2.4/shareable.html?configUrl=https://files.bpcontent.cloud/2025/05/04/07/20250504073816-NQSJEF4K.json"
        width="100%"
        height="550"
        allow="clipboard-write"
    ></iframe>
""", unsafe_allow_html=True)


