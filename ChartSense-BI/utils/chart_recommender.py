
def recommend_chart(df, question):
    q = question.lower()
    if "trend" in q or "time" in q or "monthly" in q:
        return "Line Chart"
    elif "compare" in q or "across" in q:
        return "Bar Chart"
    elif "distribution" in q:
        return "Histogram"
    elif "relationship" in q:
        return "Scatter Plot"
    else:
        return "Bar Chart"
