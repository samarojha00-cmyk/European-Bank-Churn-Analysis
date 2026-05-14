import streamlit as st
import pandas as pd

st.set_page_config(page_title="European Bank Churn Analysis")

st.title("European Bank Churn Analysis Dashboard")

st.write("Customer churn analysis project using Streamlit.")

df = pd.read_csv("Churn_Analysis_Cleaned.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Dataset Shape")
st.write(df.shape)

st.subheader("Customer Churn Distribution")
st.bar_chart(df["Exited"].value_counts())
