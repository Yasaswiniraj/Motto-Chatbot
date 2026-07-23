import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env")

client = Groq(api_key=API_KEY)


def ask_ai(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Motto, a friendly AI chatbot built by "
                        "Yasaswini. Be helpful, polite, and explain concepts "
                        "clearly for beginners."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=1024,
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Sorry! I couldn't connect to Groq.\nError: {e}"