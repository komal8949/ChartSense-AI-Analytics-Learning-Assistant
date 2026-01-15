
import streamlit as st
import pandas as pd
from utils.chart_recommender import recommend_chart
from utils.llm_explainer import explain_chart

st.set_page_config(page_title="ChartSense AI", layout="wide")

st.title("📊 ChartSense AI")
st.subheader("Your AI mentor for choosing the right Power BI visual")

uploaded_file = st.file_uploader("Upload your dataset (CSV / Excel)", type=["csv", "xlsx"])
user_question = st.text_input("Ask your analytics question (e.g. Compare sales across regions)")

if uploaded_file:
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df.head())

    if user_question:
        chart = recommend_chart(df, user_question)
        explanation = explain_chart(chart)

        st.markdown("## ✅ Recommended Chart")
        st.success(chart)

        st.markdown("## 📘 Explanation")
        st.write(explanation)
