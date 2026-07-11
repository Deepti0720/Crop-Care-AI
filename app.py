"""
Main application file for CropCare AI
This file exists to serve as the entry point for the Streamlit application.
It sets up the main configuration and navigation for the multi-page app.
It is executed directly with `streamlit run app.py`.
"""
import socket
import streamlit as st
import os


if "language" not in st.session_state:
    st.session_state.language = "English"


def internet_available():
    try:
        socket.create_connection(("8.8.8.8",53),timeout=2)
        return True
    except:
        return False
    

# Set page configuration
st.set_page_config(
    page_title="CropCare AI",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="expanded"
)
if internet_available():
    st.success("🟢 Online Mode")
else:
    st.warning("🟡 Offline Mode - Disease Detection still works.")


# Import custom CSS
def load_css():
    """
    Load custom CSS for styling the application.
    """
    css = """
    <style>
    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f1f8e9;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #2E7D32;
    }
    
    /* Cards */
    .card {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin-bottom: 20px;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #2E7D32;
        color: white;
        border-radius: 5px;
    }
    
    .stButton > button:hover {
        background-color: #1B5E20;
        color: white;
    }
    
    /* Success messages */
    .stSuccess {
        background-color: #E8F5E9;
        color: #2E7D32;
    }
    
    /* Info messages */
    .stInfo {
        background-color: #E3F2FD;
        color: #1565C0;
    }
    
    /* Warning messages */
    .stWarning {
        background-color: #FFF8E1;
        color: #FF8F00;
    }
    
    /* Error messages */
    .stError {
        background-color: #FFEBEE;
        color: #C62828;
    }
    
    /* Metrics */
    [data-testid="stMetric"] {
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 15px;
    }
    
    /* Sidebar navigation */
    [data-testid="stSidebarNav"] {
        background-color: #E8F5E9;
    }
    
    [data-testid="stSidebarNav"] ul li a {
        color: #2E7D32;
    }
    
    [data-testid="stSidebarNav"] ul li a:hover {
        background-color: #C8E6C9;
        color: #1B5E20;
    }
    
    /* Image display */
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    
    /* File uploader */
    [data-testid="stFileUploader"] {
        background-color: white;
        border-radius: 10px;
        padding: 20px;
        border: 2px dashed #81C784;
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background-color: #2E7D32;
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# Load CSS
load_css()

# Initialize session state variables
if 'language' not in st.session_state:
    st.session_state.language = "English"

if 'model_loaded' not in st.session_state:
    st.session_state.model_loaded = False

if 'model' not in st.session_state:
    st.session_state.model = None

if 'class_names' not in st.session_state:
    st.session_state.class_names = None

# Language selection in sidebar
with st.sidebar:
    st.image("https://picsum.photos/seed/cropcare/200/200.jpg", width=100)
    st.title("CropCare AI")
    st.markdown("---")
    
    language = st.selectbox(
        "Language / भाषा",
        ["English", "Hindi"],
        index=0 if st.session_state.language == "English" else 1
    )
    
    st.session_state.language = language
    
    st.markdown("---")
    st.markdown("### Navigation")
    st.markdown("Use the menu on the left to navigate between pages.")

# Display a welcome message on the main page
st.title("🌿 Welcome to CropCare AI")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ## AI-Powered Crop Disease Detection and Smart Farming Assistant
    
    CropCare AI helps farmers identify crop diseases quickly and accurately using advanced 
    machine learning techniques. 
    Simply upload an image of the affected plant, and our AI will diagnose the problem and provide treatment recommendations.""")
    


st.markdown("---")
st.markdown("### Getting Started")
st.markdown("""
1. Navigate to **Disease Detection** using the menu on the left
2. Upload an image of the affected plant or capture one using your camera
3. Click **Analyze** to get instant diagnosis and treatment recommendations
4. Explore other features like Weather Advice, Voice Assistant, and QR Scanner
""")

st.markdown("---")
st.markdown("© 2023 CropCare AI. All rights reserved.")