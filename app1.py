import streamlit as st
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="Data Dashboard", layout="wide")

# --- Custom CSS for Teal Blue Theme & Glassy Look ---
st.markdown("""
    <style>
    body {
        background-color: #e6f2f2;
        font-family: 'Poppins', sans-serif;
    }
    [data-testid="stSidebar"] {
        background: rgba(0, 128, 128, 0.1);
        backdrop-filter: blur(10px);
    }
    .main {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 20px;
        padding: 20px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: teal;
    }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.title("📊 Streamlit Data Dashboard")

# --- Sidebar Navigation ---
tabs = st.sidebar.radio("📁 Navigation", ["🏠 Home", "📈 EDA", "📊 Evaluation", "🧠 Model Testing", "⚙️ Settings"])

# --- Initialize session state for uploaded file ---
if "df" not in st.session_state:
    st.session_state.df = None

# --- HOME TAB ---
if tabs == "🏠 Home":
    st.header("Welcome to Your Data Dashboard")
    st.write("""
        This dashboard allows you to:
        - Upload and preview CSV datasets 📂  
        - Perform Exploratory Data Analysis (EDA) 📈  
        - Evaluate your data using metrics 📊  
        - Test machine learning models 🧠  
        - Customize your theme ⚙️  
    """)
    
    uploaded_file = st.file_uploader("Upload your CSV file here", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state.df = df
        st.success("✅ File successfully uploaded!")
        st.write("### Data Preview:")
        st.dataframe(df)

# --- EDA TAB ---
elif tabs == "📈 EDA":
    st.header("Exploratory Data Analysis")
    if st.session_state.df is not None:
        df = st.session_state.df
        st.subheader("Dataset Overview")
        st.write(df.describe())
        
        st.subheader("Column Information")
        st.write(df.info())
        
        st.subheader("Missing Values")
        st.write(df.isnull().sum())
    else:
        st.warning("⚠️ Please upload a CSV file in the Home tab first.")

# --- EVALUATION TAB ---
elif tabs == "📊 Evaluation":
    st.header("Data Evaluation")
    if st.session_state.df is not None:
        df = st.session_state.df
        st.write("✅ Data is ready for evaluation.")
        st.write("Shape of dataset:", df.shape)
        st.write("Columns:", list(df.columns))
    else:
        st.warning("⚠️ Please upload your data first in the Home tab.")

# --- MODEL TESTING TAB ---
elif tabs == "🧠 Model Testing":
    st.header("Model Testing")
    if st.session_state.df is not None:
        df = st.session_state.df
        st.write("Here you can test simple models (future feature).")
        st.info("🚧 This section will include model testing soon.")
    else:
        st.warning("⚠️ Please upload a CSV file first.")

# --- SETTINGS TAB ---
elif tabs == "⚙️ Settings":
    st.header("App Settings")

    theme_choice = st.radio("Choose Theme", ["🌞 Light Mode", "🌙 Dark Mode"])

    if theme_choice == "🌞 Light Mode":
        st.markdown("""
            <style>
            body { background-color: #e6f2f2 !important; color: black; }
            </style>
        """, unsafe_allow_html=True)
        st.success("✅ Light mode activated!")
    else:
        st.markdown("""
            <style>
            body { background-color: #001f1f !important; color: white !important; }
            </style>
        """, unsafe_allow_html=True)
        st.success("🌙 Dark mode activated!")

