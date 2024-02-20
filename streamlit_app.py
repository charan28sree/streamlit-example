import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Step 1: Uploading a CSV file
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file is not None:
    dataframe = pd.read_csv(uploaded_file)

    # Step 2: Representing the CSV file in a dataframe with column and row filter
    st.dataframe(dataframe)
    st.column_config.NumberColumn("Dollar values", format="$ %d")
    # You can configure other column types as well

    # Step 3: Creating a bar graph using the selected dataframe value
    selected_column = "Your_Column_Name"  # Replace with your actual column name
    val_count = dataframe[selected_column].value_counts()

    fig = plt.figure(figsize=(10, 5))
    sns.barplot(val_count.index, val_count.values, alpha=0.8)
    plt.title("Bar Chart for " + selected_column)
    plt.ylabel("Count")
    plt.xlabel("Categories")

    # Display the figure in Streamlit
    st.pyplot(fig)
