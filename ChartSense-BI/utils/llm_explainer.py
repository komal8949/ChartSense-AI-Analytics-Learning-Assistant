
def explain_chart(chart):
    explanations = {
        "Bar Chart": "Bar charts are best for comparing categories.",
        "Line Chart": "Line charts show trends over time clearly.",
        "Histogram": "Histograms show data distribution.",
        "Scatter Plot": "Scatter plots reveal relationships between variables."
    }

    avoid = {
        "Bar Chart": "Avoid bar charts for time series.",
        "Line Chart": "Avoid line charts for unordered categories.",
        "Histogram": "Avoid histograms for categorical data.",
        "Scatter Plot": "Avoid scatter plots with categorical axes."
    }

    return f"""
    Why this chart?
    {explanations.get(chart)}

    When not to use it:
    {avoid.get(chart)}

    Power BI Tip:
    Always label axes and use proper sorting.
    """
