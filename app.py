import streamlit as st
import pandas as pd

# ---- PAGE SETTINGS ----
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# ---- LOAD DATA ----
df = pd.read_csv("healthcare_cleaned.csv")

# ---- CLEAN COLUMN NAMES (IMPORTANT FIX) ----
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ---- HEADER ----
st.markdown("""
<h1 style='text-align: center; color: #1e3a8a;'>
Healthcare Risk Assessment Dashboard
</h1>
<p style='text-align: center; color: gray;'>
Analyze patient data and predict potential health risk levels
</p>
""", unsafe_allow_html=True)

st.markdown("---")

# ---- PREVIEW ----
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---- LAYOUT ----
col1, col2, col3 = st.columns(3)

# ---- DEMOGRAPHICS ----
with col1:
    st.subheader("👤 Demographics")

    age = st.slider("Age", int(df["age"].min()), int(df["age"].max()), int(df["age"].mean()))

    gender = st.radio(
        "Gender",
        sorted(df["gender"].dropna().unique())
    )

    blood = st.selectbox(
        "Blood Type",
        sorted(df["blood_type"].dropna().unique())
    )

# ---- ADMISSION ----
with col2:
    st.subheader("🏥 Admission Details")

    condition = st.selectbox(
        "Medical Condition",
        sorted(df["medical_condition"].dropna().unique())
    )

    admission = st.radio(
        "Admission Type",
        sorted(df["admission_type"].dropna().unique())
    )

# ---- FINANCE ----
with col3:
    st.subheader("💊 Treatment & Finance")

    medication = st.selectbox(
        "Medication",
        sorted(df["medication"].dropna().unique())
    )

    insurance = st.selectbox(
        "Insurance Provider",
        sorted(df["insurance_provider"].dropna().unique())
    )

    billing = st.number_input(
        "Billing Amount ($)",
        int(df["billing_amount"].min()),
        int(df["billing_amount"].max()),
        int(df["billing_amount"].mean())
    )

# ---- BUTTON ----
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Run Risk Assessment"):

    # ---- SIMPLE LOGIC ----
    if admission == "Emergency" and billing > 30000:
        result = "Critical Risk"
        color = "#ef4444"
    elif admission == "Emergency" or billing > 20000:
        result = "Moderate Risk"
        color = "#f97316"
    else:
        result = "Low Risk"
        color = "#22c55e"

    st.markdown(
        f"""
        <div style='background-color:{color}; padding:20px; border-radius:10px; text-align:center; color:white; font-size:22px;'>
        Predicted Status: {result}
        </div>
        """,
        unsafe_allow_html=True
    )