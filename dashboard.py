import streamlit as st
import requests
import pandas as pd

st.set_page_config(
    page_title="AI News Intelligence Agent",
    page_icon="🤖",
    layout="wide"
)

# HEADER
st.title("🤖 AI News Intelligence Agent")
st.markdown(
    "Analyze real-time news using a **multi-agent AI system** that searches, "
    "analyzes and extracts insights from global news."
)

st.divider()

# SIDEBAR
st.sidebar.header("⚙️ Settings")
topic = st.sidebar.text_input("Topic", "AI")
analyze_button = st.sidebar.button("🚀 Analyze News")

st.sidebar.info(
    "This system uses:\n\n"
    "- Planner Agent\n"
    "- Research Agent\n"
    "- Analyst Agent\n"
    "- Vector Memory (FAISS)"
)

# MAIN
if analyze_button:

    with st.spinner("🤖 AI agents are analyzing the news..."):

        url = "http://127.0.0.1:8000/analyze"
        params = {"topic": topic}

        response = requests.get(url, params=params)
        data = response.json()

    st.success("Analysis completed!")

    # METRICS
    colm1, colm2, colm3 = st.columns(3)

    colm1.metric("Topic", topic)
    colm2.metric("Articles Found", len(data["news"]))
    colm3.metric("Agents Used", "3")

    st.divider()

    # PLAN + ANALYSIS
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📋 Agent Plan")
        st.info(data["plan"])

    with col2:
        st.subheader("📊 AI Analysis")
        st.success(data["analysis"])

    st.divider()

    # NEWS SECTION
    st.subheader("📰 Latest News")

    for n in data["news"]:
        st.markdown(
            f"""
            <div style="padding:10px;
                        border-radius:10px;
                        border:1px solid #ddd;
                        margin-bottom:10px">
            {n}
            </div>
            """,
            unsafe_allow_html=True
        )

    st.divider()

    # SAMPLE TREND CHART
    st.subheader("📈 Trend Impact")

    data_chart = pd.DataFrame({
        "Category": ["Technology", "Finance", "Policy"],
        "Impact Score": [8, 6, 7]
    })

    st.bar_chart(data_chart.set_index("Category"))

st.divider()

st.header("💬 Chat with AI News Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Ask about news...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            url = "http://127.0.0.1:8000/analyze"

            params = {"topic": prompt}

            response = requests.get(url, params=params)

            data = response.json()

            answer = data["analysis"]

            st.markdown(answer)

    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# FOOTER
st.divider()
st.caption("⚡ Powered by Multi-Agent AI System | FastAPI + Streamlit + OpenAI")