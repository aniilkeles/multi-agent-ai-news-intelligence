from agents.llm import ask_llm

def plan_task(user_query):

    prompt = f"""
You are a planning agent.

User question:
{user_query}

Decide what steps are needed.

Return steps like:
1. Search news
2. Analyze news
3. Extract trends
"""

    return ask_llm(prompt)