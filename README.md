# 🤖 AI Chatbot with Streamlit

A simple and interactive AI-powered chatbot built using **Python**, **Streamlit**, and the **Google Gemini API**. This project provides a clean chat interface where users can ask questions and receive AI-generated responses in real time.

## 🚀 Features

* Interactive chat interface
* Real-time AI responses
* Powered by Google Gemini models
* Easy setup and deployment
* Lightweight and beginner-friendly
* Streamlit-based web application

## 🛠️ Technologies Used

* Python 3.x
* Streamlit
* Google Gemini API
* dotenv (for environment variables)

## 📂 Project Structure

```text
chat-streamlit-tutorial/
│
├── app.py              # Main Streamlit application
├── .env                # Environment variables (not tracked by Git)
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Configure API Key

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

> Never commit your API keys to GitHub.

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start locally and open in your browser.

## 💬 Usage

1. Enter your message in the chat input.
2. Submit your query.
3. Receive AI-generated responses instantly.

## 🔒 Security Notes

* Store API keys in environment variables.
* Add `.env` to `.gitignore`.
* Rotate API keys immediately if they are accidentally exposed.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome. Feel free to fork the repository and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

## 👨‍💻 Author

Developed by Yashh.
