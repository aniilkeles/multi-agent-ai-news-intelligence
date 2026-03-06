from agents.llm import ask_llm

def generate_insights(summary):

    prompt = f"""
You are an AI market analyst.

Analyze the following AI news summary and extract:

1. Key industry trends
2. Potential business impacts
3. Future predictions

Summary:
{summary}

Return the analysis in bullet points.
"""

    return ask_llm(prompt)