#📊 ChartSense AI – LLM-Powered Visualization Assistant

ChartSense AI is an AI-powered analytics learning assistant designed to help Power BI beginners choose the right chart for their data and understand why that visualization works.

Many beginners struggle with questions like:

Which chart should I use?

Why is a bar chart better than a pie chart here?

How do I explain insights correctly in Power BI?

ChartSense AI solves this by combining analytics logic + LLM-style explanations to guide users step by step.

🚀 Key Features

📂 Dataset Upload (CSV / Excel)

💬 Natural Language Analytics Questions

📈 Smart Chart Recommendations

📘 Beginner-Friendly Explanations

⚠️ When NOT to use a chart

🎯 Power BI–specific visualization tips

🧠 How It Works

User uploads a dataset (CSV / Excel)

User asks an analytics question
Example:

“Compare sales across regions”

ChartSense AI:

Analyzes the intent

Recommends the best chart

Explains why

Explains why other charts are not ideal

Gives Power BI best practices

🏗️ Project Architecture
ChartSense_AI/
│
├── app.py                     # Streamlit application
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
│
└── utils/
    ├── chart_recommender.py   # Chart recommendation logic
    └── llm_explainer.py       # Explanation engine

🛠️ Tech Stack

Frontend / UI: Streamlit

Backend: Python

Data Handling: Pandas

AI Logic: Rule-based + LLM-style explanations

Deployment Ready: Streamlit Cloud / Local

▶️ Run Locally
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py


The app will start at:

http://localhost:8501

📌 Example Use Case

User Question:

Compare revenue across regions

ChartSense AI Output:

✅ Recommended Chart: Bar Chart

📘 Why: Best for comparing categorical values

⚠️ Avoid: Line chart (no time-based trend)

🎯 Power BI Tip: Sort regions by revenue for clarity

🎯 Target Users

Power BI beginners

Data analytics students

Business analysts

Freshers learning data visualization

Anyone confused about chart selection

🌱 Future Enhancements

🔗 LLM integration (OpenAI / LLaMA / Mistral)

📚 RAG-based analytics knowledge base

🧠 Automatic column-type detection

📊 Power BI field mapping suggestions

📈 Visual preview generation
