import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
def main():
    st.title("CSV File Uploader and Filters")

    # File uploader
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file:
        # Read CSV data into a DataFrame
        df = pd.read_csv(uploaded_file)

        # Display column names
        st.write("Column Names:")
        st.write(df.columns.tolist())

        # Display distinct row values for each column
        st.write("Distinct Row Values:")
        for col in df.columns:
            st.write(f"{col}: {df[col].unique().tolist()}")

        # Add filters (you can customize this part)
        selected_columns = st.multiselect("Select columns to display", df.columns)
        filtered_df = df[selected_columns]

        # Display filtered DataFrame
        st.dataframe(filtered_df)

if __name__ == "__main__":
    main()
