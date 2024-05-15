import streamlit as st
import pandas as pd

# Load the data
data_path = 'compiled_checklist.csv'
df = pd.read_csv(data_path)

# Set up the Streamlit app
st.title("Employee Checklist Dashboard")

# Sidebar for selecting candidates
st.sidebar.title("Select Candidates")
candidates = df.columns[2:-1]  # Exclude the first two and last columns
selected_candidates = st.sidebar.multiselect("Candidates", candidates, default=candidates[:2])

# Display selected candidates' responses
if selected_candidates:
    selected_data = df[['Details', 'Sharaf DG candidate checklist - Requirement'] + selected_candidates]
    st.write(selected_data)
else:
    st.write("Please select at least one candidate to compare.")

# Allow user to add comments to individual responses
st.sidebar.title("Add Comments")
selected_row = st.sidebar.selectbox("Select Question", df['Details'].unique())
comment = st.sidebar.text_area("Comment", "")

if st.sidebar.button("Save Comment"):
    st.write(f"Comment saved for question '{selected_row}': {comment}")

# Note: You will need to implement a mechanism to save comments to a persistent storage
# This is just a basic example to get started
