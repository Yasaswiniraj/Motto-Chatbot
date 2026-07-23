# 🤖 Motto - AI Chatbot

Motto is a beginner-friendly AI chatbot built with **Python**. It combines **rule-based responses** with **LLM-powered AI** using the **Groq API**, making conversations both fast and intelligent.

This project was built to learn Python, APIs, software architecture, and AI chatbot development from scratch.

---

# 🚀 Features

### 💬 Basic Conversation
- Greetings
- Goodbye messages
- Thank you responses
- Help command

### 🧠 Smart Memory
- Remembers your name during the chat
- Personalized greetings
- Forget your name command

### 🎯 Built-in Responses
- Programming (Python, Java, AI)
- Date
- Time
- College
- Weather
- Food
- Music
- Favorite Color

### 🎲 Random Responses
- Programming jokes
- Motivational quotes
- Friendly greetings

### 🤖 AI Integration
- Groq API
- Llama 3.3 70B Versatile Model
- Intelligent responses for unknown questions

### 🔒 Secure
- API keys stored using `.env`
- `.gitignore` prevents secrets from being uploaded

---

# 🛠️ Tech Stack

- Python 3
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv
- VS Code
- Git & GitHub

---

# 📂 Project Structure

```text
Motto-Chatbot/
│
├── data/
│   ├── greetings.py
│   ├── jokes.py
│   └── quotes.py
│
├── ai.py
├── chatbot.py
├── responses.py
├── main.py
├── requirements.txt
├── README.md
├── .env
└── .gitignore
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Yasaswiniraj/Motto-Chatbot.git
```

---

## 2️⃣ Navigate to the Project

```bash
cd Motto-Chatbot
```

---

## 3️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

## 4️⃣ Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 6️⃣ Create a `.env` File

Create a file named `.env` in the project root.

```env
GROQ_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your Groq API key.

---

## 7️⃣ Run the Chatbot

```bash
python main.py
```

---

# 💬 Sample Conversation

```text
=============================================
🤖 Motto Chatbot
Type 'exit' to quit.
=============================================

You : Hi
Bot : Hello! 👋

You : My name is Yasaswini
Bot : Nice to meet you, Yasaswini! 😊 I'll remember your name while we're chatting.

You : What is my name?
Bot : Your name is Yasaswini.

You : Tell me a joke
Bot : Why do programmers prefer dark mode?
      Because light attracts bugs! 😂

You : Explain Recursion

Bot :
Recursion is a programming technique where a function calls itself...
```

---

# 📦 Dependencies

```text
groq
python-dotenv
```

---

# 🏗️ Project Architecture

```text
                User
                  │
                  ▼
            Motto Chatbot
                  │
      ┌───────────┴───────────┐
      │                       │
 Rule-based Engine      AI Engine (Groq)
      │                       │
      └───────────┬───────────┘
                  ▼
             Final Response
```

---

# 🎯 Current Version

## Version 3.0

### Completed

- Rule-based chatbot
- Random greetings
- Programming jokes
- Motivational quotes
- Date & Time
- Temporary memory
- Modular codebase
- AI integration with Groq
- Environment variables
- Hybrid chatbot architecture

---

# 🚀 Future Roadmap

### Version 4

- Flask Web App
- Beautiful Chat Interface
- Chat History
- Persistent Memory
- Markdown Rendering
- Voice Input
- Voice Output
- File Upload Support
- Image Understanding
- User Authentication
- Database Integration

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to GitHub
5. Open a Pull Request

---

# 👩‍💻 Author

**Yasaswini Raj**

B.Tech Computer Science Student

Python • AI • Machine Learning • Open Source

GitHub:
https://github.com/Yasaswiniraj

---

# ⭐ Support

If you enjoyed this project, consider giving it a ⭐ on GitHub!

It helps others discover the project and motivates further development.

---

# 📄 License

This project is licensed under the MIT License.