import streamlit as st
import os

st.title("CX-VOC Data Uploader")

# Secure access for you only
password = st.text_input("Enter Upload Password", type="password")

if password != "Metro_CRM":  # 🔐 Change this to your actual password
    st.warning("Unauthorized access")
    st.stop()

uploaded_file = st.file_uploader("Upload your latest CSV file", type=["csv"])

if uploaded_file:
    with open("latest_data.csv", "wb") as f:
        f.write(uploaded_file.read())
    st.success("Upload complete! CSV saved as latest_data.csv")
