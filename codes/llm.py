import os
from pathlib import Path
from openai import OpenAI


BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_PATH = BASE_DIR / "docs" / "peanut_butter_system_prompt.md"


with open(PROMPT_PATH, "r", encoding="utf-8") as f:
    personality_prompt = f.read()


api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise RuntimeError("DEEPSEEK_API_KEY is not set.")


client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)

messages = [
    {
        "role": "system",
        "content": personality_prompt
    }
]

def chat(user_message):
    messages.append({
        "role": "user",
        "content": user_message
    })

    response = client.chat.completions.create(
        model="deepseek-flash",
        messages=messages
    )

    reply = response.choices[0].message.content

    messages.append({
        "role": "assistant",
        "content": reply
    })

    return reply

