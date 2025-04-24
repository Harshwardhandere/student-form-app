# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import os

# GitHub CSV URL (replace with your repository URL)
github_csv_url = 'https://github.com/Harshwardhandere/student-registration/blob/main/students_data.csv'

# Check if the CSV file exists on GitHub or locally
csv_file = "students_data.csv"
if os.path.exists(csv_file):
    st.subheader("📊 Submitted Data")
    data = pd.read_csv(csv_file)  # Read the local CSV file
    st.dataframe(data)

st.title("🎓 Student Registration Form")

# Initialize the CSV file if it doesn't exist (locally)
if not os.path.exists(csv_file):
    columns = ["Name", "Gender", "Education"]
    df = pd.DataFrame(columns=columns)
    df.to_csv(csv_file, index=False)  # Create an empty CSV file with columns

# Form inputs
name = st.text_input("Name")
gender = st.radio("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Undergraduate", "Postgraduate", "Higher Education"])

if st.button("Submit"):
    if name == "":
        st.warning("Please enter a name.")
    else:
        # Read the existing data from the CSV file
        data = pd.read_csv(csv_file)

        # Append the new data
        new_data = pd.DataFrame([[name, gender, education]], columns=["Name", "Gender", "Education"])
        data = pd.concat([data, new_data], ignore_index=True)

        # Save the updated data back to the CSV file
        data.to_csv(csv_file, index=False)

        # Optionally, push the updated CSV file to GitHub (you can automate this if needed)
        st.success(f"✅ Data saved for {name}")





