# 🤖 AI Product Chatbot API

<p align="center">
  <img src="https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png" width="80">
</p>

<p align="center">
AI-powered product chatbot built with Python and modular agent architecture — designed for website integration, mobile demos, and scalable serverless deployment.
</p>

---

## 📌 About This Project

This project is a **Python-based AI chatbot system** designed to handle product-related queries through a clean API interface.  
It is built with a **modular agent architecture**, allowing easy expansion for FAQs, products, and business logic.

The chatbot is production-ready and supports:

- Website chatbot integration  
- Mobile live demo access  
- Serverless deployment on Vercel  
- Static frontend hosting via GitHub Pages  

---

## 🧠 Features

- 💬 Intelligent product-based chatbot agent  
- 🧩 Modular agent architecture  
- 📦 Product & FAQ knowledge base  
- 🌐 REST API endpoints (`/api/chat`, `/api/health`)  
- ⚡ Serverless backend deployment (Vercel)  
- 🖥️ Static chat widget frontend  
- 📱 Mobile-friendly live demo  
- 🔐 Environment-based configuration  

---

## 🚀 Tech Stack / Tools Used

![Python](https://img.shields.io/badge/Python-3670A0?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?logo=vercel&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-239120?logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)
![GitHub Pages](https://img.shields.io/badge/GitHub_Pages-222222?logo=githubpages&logoColor=white)

---

## 📂 Project Structure

chatbot-api/
├── app.py Application entrypoint (API server)
├── main.py Local development runner
├── requirements.txt Python dependencies
├── vercel.json Vercel deployment configuration
├── agents/
│ ├── init.py
│ └── product_agent.py Product chatbot agent logic
├── api/
│ └── init.py API routing layer
├── config/
│ ├── init.py
│ └── settings.py Environment & app settings
├── data/
│ ├── init.py
│ ├── faqs.py FAQ dataset
│ └── products.py Product dataset
├── static/
│ └── chat-widget.html Frontend chat widget (HTML + JS)
├── utils/
│ ├── init.py
│ └── helpers.py Shared helper utilities
└── README.md Project documentation

---

## 🌐 Live Demo

### 🔹 Chatbot Frontend (Mobile & Web)
https://umer-206.github.io/chatbot-api/static/chat-widget.html


### 🔹 Backend API (Vercel)
https://chatbot-api-sigma-lyart.vercel.app

---

## 🔌 API Usage

### Chat Endpoint
**POST**

#### Request Body:
```json
{
  "message": "Show me available products",
  "session_id": "unique_user_id"
}

Request Body
{
  "response": "Here is the product list...",
  "session_id": "unique_user_id"
}

#### Request Body:


