from openai import OpenAI
import os
import json
from dotenv import load_dotenv
from tools.news_search import search_news

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def run_agent(user_query):

    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_news",
                "description": "Search latest news about a topic",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "topic": {
                            "type": "string",
                            "description": "Topic to search news for"
                        }
                    },
                    "required": ["topic"]
                }
            }
        }
    ]

    messages = [
        {"role": "system", "content": "You are an AI research agent."},
        {"role": "user", "content": user_query}
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:

        tool_call = message.tool_calls[0]

        args = json.loads(tool_call.function.arguments)

        news = search_news(args["topic"])

        messages.append(message)

        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": "\n".join(news)
            }
        )

        final_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages
        )

        return news, final_response.choices[0].message.content

    else:
        return [], message.content