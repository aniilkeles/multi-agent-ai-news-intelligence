from agents.planner_agent import plan_task
from agents.research_agent import research_topic
from agents.analyst_agent import analyze_news

query = input("Ask the AI system: ")

print("\nPLANNER AGENT:\n")

plan = plan_task(query)

print(plan)

print("\nRESEARCH AGENT:\n")

news = research_topic(query)

for n in news:
    print(n)

print("\nANALYST AGENT:\n")

analysis = analyze_news(news)

print(analysis)