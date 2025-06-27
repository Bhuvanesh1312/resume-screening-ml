import streamlit as st
from scripts.predict import predict_role

st.set_page_config(page_title="Resume Screening", layout="centered")

st.title("📄 Resume Screening System using ML")
st.write("Upload a resume in PDF format and get the predicted job role.")

uploaded_file = st.file_uploader("Upload a resume", type="pdf")

if uploaded_file is not None:
    with open("temp_resume.pdf", "wb") as f:
        f.write(uploaded_file.read())
    with st.spinner("Analyzing resume..."):
        result = predict_role("temp_resume.pdf")
    st.success(f"🎯 Predicted Role: **{result}**")
