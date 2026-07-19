from responses import get_response


def chat():
    print("=" * 45)
    print("🤖 Motto Chatbot")
    print("Type 'exit' to quit.")
    print("=" * 45)

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Goodbye! 👋")
            break

        response = get_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    chat()