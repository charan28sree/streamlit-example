import streamlit as st
import pandas as pd

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


# Step 1: Upload a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Step 2: Select columns and filter rows
    selected_columns = st.multiselect("Select columns", df.columns)
    filtered_df = df[selected_columns]

    min_row, max_row = st.slider("Select row range", 0, len(df), (0, len(df)))
    filtered_df = filtered_df.iloc[min_row:max_row]

        # Step 3: Add a new "Reporting Period" column
    reporting_periods = filtered_df["Reporting Period"].unique()
    selected_reporting_period = st.selectbox("Select a reporting period", reporting_periods)

    # Step 4: Create a bar chart
    st.bar_chart(filtered_df)
