import os

from dotenv import load_dotenv
from google import genai

# Load variables from .env
load_dotenv()

# Read the API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=API_KEY)


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text