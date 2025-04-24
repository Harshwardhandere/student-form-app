# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("your-credentials.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Student Data").sheet1  # Make sure this Sheet exists & is shared with the service account email

# Streamlit form
st.title("🎓 Student Registration Form")
name = st.text_input("Name")
gender = st.radio("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Undergraduate", "Postgraduate", "Higher Education"])

if st.button("Submit"):
    if name == "":
        st.warning("Please enter a name.")
    else:
        sheet.append_row([name, gender, education])
        st.success(f"✅ Data saved for {name}")

# Display existing data
st.subheader("📊 Submitted Data")
data = pd.DataFrame(sheet.get_all_records())
st.dataframe(data)




