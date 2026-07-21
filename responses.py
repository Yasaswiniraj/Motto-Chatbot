import random
from datetime import datetime

from data.greetings import greetings
from data.jokes import jokes
from data.quotes import quotes


def get_response(user_input):
    message = user_input.lower().strip()

    responses = {
        "morning": "Good morning! ☀️ Hope you have a wonderful day!",
        "night": "Good night! 🌙 Sweet dreams!",
        "who are you": "I'm Motto, your friendly chatbot. 🤖",
        "what is your name": "My name is Motto. Nice to meet you! 😊",
        "how are you": "I'm doing great! Thanks for asking. 😊",
        "who made you": "I was built by Yasaswini using Python. 🚀",
        "thank you": "You're welcome! 😊",
        "thanks": "Happy to help! 😄",
        "help": """
I can help you with:

👋 Greetings
😂 Jokes
💻 Programming
🌟 Motivation
📅 Date
⏰ Time

Type 'exit' anytime to quit.
"""
    }

    # Exact matches
    if message in responses:
        return responses[message]

    # Greetings
    if any(word in message for word in ["hi", "hello", "hey"]):
        return random.choice(greetings)

    # Goodbye
    if any(word in message for word in ["bye", "goodbye", "see you"]):
        return random.choice([
            "Goodbye! Have a wonderful day! 👋",
            "See you soon! 😊",
            "Take care! 🌸",
            "Bye! Keep smiling! 😄"
        ])

    # Python
    if "python" in message:
        return (
            "Python is a beginner-friendly, powerful programming language "
            "used in AI, Machine Learning, Web Development, Automation, and more."
        )

    # Java
    if "java" in message:
        return (
            "Java is an object-oriented programming language widely used for "
            "DSA, backend development, Android apps, and enterprise software."
        )

    # AI
    if any(word in message for word in ["ai", "artificial intelligence"]):
        return (
            "Artificial Intelligence enables computers to perform tasks that "
            "normally require human intelligence, such as learning and problem-solving."
        )

    # College
    if "college" in message:
        return "College is a place to learn, explore, build projects, and grow your skills. 🎓"

    # Joke
    if "joke" in message:
        return random.choice(jokes)

    # Motivation
    if any(word in message for word in ["motivate", "motivation", "quote", "inspire"]):
        return random.choice(quotes)

    # Time
    if "time" in message:
        return datetime.now().strftime("🕒 Current Time: %I:%M %p")

    # Date
    if "date" in message:
        return datetime.now().strftime("📅 Today's Date: %d-%m-%Y")

    # Weather
    if "weather" in message:
        return "Sorry! I can't check live weather yet. 🌦️"

    # Favorite color
    if "favorite color" in message:
        return "I like blue because it reminds me of technology and creativity. 💙"

    # Food
    if any(word in message for word in ["food", "pizza", "burger"]):
        return "I don't eat food, but pizza does look delicious! 🍕"

    # Music
    if "music" in message:
        return "I enjoy every kind of music—even though I can't actually hear it! 🎵"

    # Unknown responses
    unknown = [
        "🤔 I'm still learning. Could you ask that differently?",
        "😊 That's interesting! I don't know the answer yet.",
        "🚀 I'm learning new things every day!",
        "💡 Sorry, I don't understand that yet.",
        "😄 Can you rephrase your question?"
    ]

    return random.choice(unknown)