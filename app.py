import streamlit as st
import pandas as pd

# ---- PAGE SETTINGS ----
st.set_page_config(page_title="Healthcare Dashboard", layout="wide")

# ---- LOAD DATASET ----
df = pd.read_csv("healthcare_cleaned.csv")

# ---- STYLE ----
st.markdown("""
<style>
body {
    background-color: #f5f7fb;
}
.block-container {
    padding-top: 2rem;
}

/* Header */
.header {
    text-align: center;
    padding: 10px;
}
.header h1 {
    color: #1e3a8a;
}
.header p {
    color: #6b7280;
    font-size: 18px;
}

/* Cards */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.05);
}

/* Section Titles */
.section-title {
    color: #1e40af;
    font-weight: 600;
}

/* Button */
.stButton>button {
    background-color: #2563eb;
    color: white;
    font-size: 18px;
    border-radius: 10px;
    padding: 10px 20px;
}

/* Result */
.result-green {
    background-color: #22c55e;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    color: white;
    margin-top: 20px;
}
.result-orange {
    background-color: #f97316;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    color: white;
    margin-top: 20px;
}
.result-red {
    background-color: #ef4444;
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    color: white;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div class="header">
    <h1>Healthcare Risk Assessment Dashboard</h1>
    <p>Analyze patient data and predict potential health risk levels</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ---- SHOW DATA (optional but good) ----
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ---- LAYOUT ----
col1, col2, col3 = st.columns(3)

# ---- DEMOGRAPHICS ----
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">👤 Demographics</div>', unsafe_allow_html=True)
    
    age = st.slider("Age", 0, 100, 35)
    gender = st.radio("Gender", sorted(df["gender"].dropna().unique()))
    blood = st.selectbox("Blood Type", sorted(df["bloodtype"].dropna().unique()))
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---- ADMISSION ----
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">🏥 Admission Details</div>', unsafe_allow_html=True)
    
    condition = st.selectbox("Medical Condition", sorted(df["medicalcondition"].dropna().unique()))
    admission = st.radio("Admission Type", sorted(df["admissiontype"].dropna().unique()))
    stay = st.slider("Length of Stay (days)", 1, 30, 5)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---- FINANCE ----
with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">💊 Treatment & Finance</div>', unsafe_allow_html=True)
    
    medication = st.selectbox("Medication", sorted(df["medication"].dropna().unique()))
    insurance = st.selectbox("Insurance Provider", sorted(df["insuranceprovider"].dropna().unique()))
    billing = st.number_input("Billing Amount ($)", 0, 100000, 10000)
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---- BUTTON ----
st.markdown("<br>", unsafe_allow_html=True)

if st.button("🔍 Run Risk Assessment"):

    # ---- LOGIC ----
    if admission == "Emergency" and billing > 30000:
        result = "Critical Risk"
        css = "result-red"
    elif admission == "Emergency" or billing > 20000:
        result = "Moderate Risk"
        css = "result-orange"
    else:
        result = "Low Risk"
        css = "result-green"

    st.markdown(
        f'<div class="{css}">⚠️ Predicted Status: {result}</div>',
        unsafe_allow_html=True
    )