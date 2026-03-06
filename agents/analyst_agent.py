from agents.llm import ask_llm
from memory.vector_store import add_memory, search_memory

def analyze_news(news):

    text = "\n".join(news)

    past_memory = search_memory(text)

    prompt = f"""
You are an AI analyst.

Previous related analyses:
{past_memory}

Current news:
{text}

Analyze trends and business impacts.
"""

    analysis = ask_llm(prompt)

    add_memory(analysis)

    return analysis