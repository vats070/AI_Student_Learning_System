
import streamlit as st


def load_styles():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --purple: #4b0dbb;
        --dark-purple: #21045c;
        --page-bg: #f2f5ff;
        --border: #dcd9ee;
        --text: #454653;
        --muted: #858595;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: var(--page-bg);
        color: #303044;
    }

    /* Header */
    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1600px;
        padding: 1rem 3rem 2rem 3rem;
    }

    #MainMenu, footer {
        visibility: hidden;
    }

    .dashboard-header {
        background: var(--dark-purple);
        padding: 20px 28px;
        border-radius: 15px;
        color: white;
        margin-bottom: 25px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 15px;
        flex-wrap: wrap;
        box-shadow: 0 5px 18px rgba(33,4,92,.10);
    }

    .brand {
        font-size: 22px;
        font-weight: 800;
        letter-spacing: -.5px;
        color: #ffffff !important;
    }

    .brand-subtitle {
        font-size: 12px;
        color: #c8b9ec !important;
        margin-top: 5px;
    }

    .header-right {
        font-size: 12px;
        color: #e3dafa !important;
    }

    /* Section headings */
    .section-title {
        color: #454653 !important;
        font-size: 20px;
        font-weight: 750;
        margin-top: 8px;
        margin-bottom: 15px;
    }

    .section-subtitle {
        color: #686879 !important;
        font-size: 12px;
        margin-top: -10px;
        margin-bottom: 18px;
    }

    /* Containers */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 13px;
        box-shadow: 0 2px 8px rgba(41, 27, 91, .025);
    }

    /* Academic overview cards */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 12px;
        padding: 17px 18px;
        min-height: 115px;
    }

    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] *,
    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] * {
        color: #303044 !important;
        -webkit-text-fill-color: #303044 !important;
        opacity: 1 !important;
    }

    div[data-testid="stMetricLabel"] {
        font-size: 13px !important;
        font-weight: 600 !important;
    }

    div[data-testid="stMetricValue"] {
        font-weight: 800 !important;
        font-size: 27px !important;
    }

    div[data-testid="stMetricDelta"] {
        font-size: 12px;
    }

    /* Model evaluation caption */
    .stApp [data-testid="stCaptionContainer"],
    .stApp [data-testid="stCaptionContainer"] * {
        color: #454653 !important;
        -webkit-text-fill-color: #454653 !important;
        opacity: 1 !important;
    }

    /* FIX: Streamlit number input and slider labels */
    .stApp [data-testid="stWidgetLabel"],
    .stApp [data-testid="stWidgetLabel"] *,
    .stApp [data-testid="stSlider"] label,
    .stApp [data-testid="stSlider"] label *,
    .stApp [data-testid="stNumberInput"] label,
    .stApp [data-testid="stNumberInput"] label *,
    .stApp [data-testid="stWidgetLabel"] p {
        color: #303044 !important;
        -webkit-text-fill-color: #303044 !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* FIX: Subject-level scores and Markdown text */
    .stApp [data-testid="stMarkdownContainer"] p,
    .stApp [data-testid="stMarkdownContainer"] strong,
    .stApp [data-testid="stMarkdownContainer"] h1,
    .stApp [data-testid="stMarkdownContainer"] h2,
    .stApp [data-testid="stMarkdownContainer"] h3 {
        color: #303044 !important;
        -webkit-text-fill-color: #303044 !important;
    }

    /* Input controls */
    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] {
        border-radius: 8px;
        color: #303044 !important;
        -webkit-text-fill-color: #303044 !important;
    }

    .stSlider [data-baseweb="slider"] {
        padding-top: 8px;
    }

    /* Buttons */
    div.stButton > button,
    div.stFormSubmitButton > button {
        background: var(--purple);
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 0;
        border-radius: 9px;
        font-weight: 650;
        padding: 10px 16px;
        transition: .2s ease;
    }

    div.stButton > button:hover,
    div.stFormSubmitButton > button:hover {
        background: #35058d;
        color: #ffffff !important;
        border: 0;
    }

    /* Data table */
    div[data-testid="stDataFrame"] {
        border: 1px solid var(--border);
        border-radius: 9px;
        overflow: hidden;
    }

    /* Images */
    div[data-testid="stImage"] {
        border-radius: 10px;
    }

    @media (max-width: 900px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .dashboard-header {
            padding: 18px;
        }

        .brand {
            font-size: 19px;
        }
    }
    
    
    
    /* Make only Study hours input text white */
    .stApp [data-testid="stNumberInput"] input {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }
    


    /* Fix Predict Performance button inside the form */
    .stApp [data-testid="stForm"] button[kind="primaryFormSubmit"],
    .stApp [data-testid="stForm"] button[data-testid="stFormSubmitButton"],
    .stApp [data-testid="stFormSubmitButton"] button,
    .stApp form button {
        background: #4b0dbb !important;
        background-color: #4b0dbb !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        border: 1px solid #4b0dbb !important;
        opacity: 1 !important;
    }

    /* Force the text and nested elements to remain white */
    .stApp [data-testid="stForm"] button[kind="primaryFormSubmit"] *,
    .stApp [data-testid="stFormSubmitButton"] button *,
    .stApp form button span,
    .stApp form button p {
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        opacity: 1 !important;
    }

    /* Hover effect */
    .stApp [data-testid="stForm"] button:hover,
    .stApp [data-testid="stFormSubmitButton"] button:hover,
    .stApp form button:hover {
        background: #35058d !important;
        background-color: #35058d !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
    }

    </style>
    """, unsafe_allow_html=True)

    