def get_response(user_input):
    message = user_input.lower().strip()

    responses = {
        "hi": "Hello! 👋",
        "hello": "Hi there! 😊",
        "hey": "Hey! How can I help you?",
        "morning": "Good morning! ☀️",
        "night": "Good night! 🌙",
        "who are you": "I'm Motto,friendly chatbot. 🤖",
        "how are you": "I'm doing great! Thanks for asking. 😊",
        "what is your name": "I'm Motto, your friendly chatbot.",
        "who made you": "I was built by Yasaswini using Python. 🚀",
        "bye": "Goodbye! Have a wonderful day! 👋",
        "thank you": "You're welcome! 😊",
        "thanks": "Happy to help!",
    }

    if message in responses:
        return responses[message]

    if "college" in message:
        return "College life is full of learning and fun!"

    if "python" in message:
        return "Python is one of the easiest and most powerful programming languages."

    if "java" in message:
        return "Java is widely used for software development and DSA."

    if "weather" in message:
        return "Sorry, I can't check live weather yet."

    if "time" in message:
        return "I can't tell the current time yet."

    return "I'm sorry, I don't understand that yet. 🤔"