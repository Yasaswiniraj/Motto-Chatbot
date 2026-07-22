import random
from datetime import datetime

from data.greetings import greetings
from data.jokes import jokes
from data.quotes import quotes

# Temporary memory
user_name = None


def get_response(user_input):
    global user_name

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

✨ I can even remember your name while we're chatting!

Commands:
• My name is ...
• What is my name?
• Who am I?
• Forget my name

Type 'exit' anytime to quit.
"""
    }

    # -----------------------------
    # Name Memory
    # -----------------------------

    if message.startswith("my name is "):
        name = user_input[11:].strip()

        if name:
            user_name = name.title()
            return f"Nice to meet you, {user_name}! 😊 I'll remember your name while we're chatting."

        return "I couldn't catch your name."

    if "what is my name" in message:
        if user_name:
            return f"Your name is {user_name}. 😊"
        return "I don't know your name yet. Tell me by saying 'My name is ...'"

    if "who am i" in message:
        if user_name:
            return f"You are {user_name}! 😄"
        return "I don't know your name yet."

    if "forget my name" in message:
        if user_name:
            user_name = None
            return "Done! I've forgotten your name. 😊"
        return "I don't know your name yet."

    # -----------------------------
    # Exact Responses
    # -----------------------------

    if message in responses:
        return responses[message]

    # -----------------------------
    # Greetings
    # -----------------------------

    if any(word in message for word in ["hi", "hello", "hey"]):
        greeting = random.choice(greetings)

        if user_name:
            return f"{greeting} Nice to see you again, {user_name}! 😊"

        return greeting

    # -----------------------------
    # Goodbye
    # -----------------------------

    if any(word in message for word in ["bye", "goodbye", "see you"]):
        return random.choice([
            "Goodbye! Have a wonderful day! 👋",
            "See you soon! 😊",
            "Take care! 🌸",
            "Bye! Keep smiling! 😄"
        ])

    # -----------------------------
    # Programming
    # -----------------------------

    if "python" in message:
        return (
            "Python is a beginner-friendly, powerful programming language "
            "used in AI, Machine Learning, Web Development, Automation, and more."
        )

    if "java" in message:
        return (
            "Java is an object-oriented programming language widely used for "
            "DSA, backend development, Android apps, and enterprise software."
        )

    if any(word in message for word in ["ai", "artificial intelligence"]):
        return (
            "Artificial Intelligence enables computers to perform tasks that "
            "normally require human intelligence, such as learning and problem-solving."
        )

    # -----------------------------
    # College
    # -----------------------------

    if "college" in message:
        return "College is a place to learn, explore, build projects, and grow your skills. 🎓"

    # -----------------------------
    # Jokes
    # -----------------------------

    if "joke" in message:
        return random.choice(jokes)

    # -----------------------------
    # Motivation
    # -----------------------------

    if any(word in message for word in ["motivate", "motivation", "quote", "inspire"]):
        return random.choice(quotes)

    # -----------------------------
    # Date & Time
    # -----------------------------

    if "time" in message:
        return datetime.now().strftime("🕒 Current Time: %I:%M %p")

    if "date" in message:
        return datetime.now().strftime("📅 Today's Date: %d-%m-%Y")

    # -----------------------------
    # Miscellaneous
    # -----------------------------

    if "weather" in message:
        return "Sorry! I can't check live weather yet. 🌦️"

    if "favorite color" in message:
        return "I like blue because it reminds me of technology and creativity. 💙"

    if any(word in message for word in ["food", "pizza", "burger"]):
        return "I don't eat food, but pizza does look delicious! 🍕"

    if "music" in message:
        return "I enjoy every kind of music—even though I can't actually hear it! 🎵"

    # -----------------------------
    # Unknown Responses
    # -----------------------------

    unknown = [
        "🤔 I'm still learning. Could you ask that differently?",
        "😊 That's interesting! I don't know the answer yet.",
        "🚀 I'm learning new things every day!",
        "💡 Sorry, I don't understand that yet.",
        "😄 Can you rephrase your question?"
    ]

    return random.choice(unknown)