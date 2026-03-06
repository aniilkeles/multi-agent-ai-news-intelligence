# 🤖 Multi-Agent AI News Intelligence

A full-stack AI system that retrieves and analyzes real-time news using a **multi-agent architecture** powered by LLMs.

Users can enter a topic and the system will automatically search for related news, analyze trends, and generate insights through multiple AI agents.

---

## 🚀 Features

- **Multi-Agent Architecture**
  - Planner Agent
  - Research Agent
  - Analyst Agent
- Real-time news retrieval
- AI-powered trend and insight analysis
- Vector memory using **FAISS**
- **FastAPI** backend
- Interactive **Streamlit dashboard**
- AI chat interface

---

## 🏗 Architecture

User  
↓  
Streamlit Dashboard  
↓  
FastAPI Backend  
↓  
Planner Agent  
↓  
Research Agent  
↓  
Analyst Agent  
↓  
Vector Memory (FAISS)  
↓  
OpenAI LLM

---

## 📂 Project Structure


multi-agent-ai-news-intelligence
│
├── agents
│ ├── planner_agent.py
│ ├── research_agent.py
│ └── analyst_agent.py
│
├── memory
│ └── vector_store.py
│
├── tools
│ └── news_search.py
│
├── dashboard.py
├── app.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md


---

## ⚙️ Installation

Clone the repository:


git clone https://github.com/aniilkeles/multi-agent-ai-news-intelligence.git

cd multi-agent-ai-news-intelligence


Install dependencies:


pip install -r requirements.txt


---

## 🔑 Environment Variables

Create a `.env` file in the project root:


OPENAI_API_KEY=your_openai_api_key
NEWS_API_KEY=your_news_api_key


⚠️ Never upload your API keys to GitHub.

---

## ▶️ Run the Project

Start the FastAPI backend:


uvicorn app:app --reload


Start the Streamlit dashboard:


streamlit run dashboard.py


Open in your browser:


http://localhost:8501


---

## 🧪 Example Topics

You can test the system with topics such as:

- AI
- Tesla
- Crypto
- Nvidia
- SpaceX

The AI agents will automatically retrieve news, analyze trends, and generate insights.

---

## 🛠 Tech Stack

- Python
- FastAPI
- Streamlit
- OpenAI API
- FAISS Vector Database
- Sentence Transformers
- Requests

---

## 👨‍💻 Author

**Anıl Keleş**  
AI Engineer | Machine Learning | LLM Systems  

GitHub: https://github.com/aniilkeles
