def get_response(user_input):
    message = user_input.lower().strip()

    responses = {
        "hi": "Hello! 👋",
        "hello": "Hi there! 😊",
        "hey": "Hey! How can I help you?",
        "morning": "Good morning! ☀️",
        "night": "Good night! 🌙",
        "who are you": "I'm Motto, your friendly chatbot. 🤖",
        "how are you": "I'm doing great! Thanks for asking. 😊",
        "what is your name": "I'm Motto, your friendly chatbot.",
        "who made you": "I was built by Yasaswini using Python. 🚀",
        "bye": "Goodbye! Have a wonderful day! 👋",
        "thank you": "You're welcome! 😊",
        "thanks": "Happy to help!",
    }

    # Exact match
    if message in responses:
        return responses[message]

    # Greetings
    if any(word in message for word in ["hi", "hello", "hey"]):
        return "Hello! 👋"

    # Goodbye
    if any(word in message for word in ["bye", "goodbye", "see you"]):
        return "Goodbye! Have a great day! 👋"

    # Python
    if any(word in message for word in ["python", "py"]):
        return "Python is an easy and powerful programming language."

    # Java
    if "java" in message:
        return "Java is excellent for DSA and backend development."

    # Thanks
    if any(word in message for word in ["thank", "thanks"]):
        return "You're welcome! 😊"

    # Default response
    return "I'm not sure how to answer that yet. Could you ask something else?"