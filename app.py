from fastapi import FastAPI
from agents.planner_agent import plan_task
from agents.research_agent import research_topic
from agents.analyst_agent import analyze_news

app = FastAPI()

@app.get("/analyze")

def analyze(topic: str):

    plan = plan_task(topic)

    news = research_topic(topic)

    analysis = analyze_news(news)

    return {
        "plan": plan,
        "news": news,
        "analysis": analysis
    }