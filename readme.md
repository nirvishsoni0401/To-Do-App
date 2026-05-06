# ✅ To-Do App

A clean, full-stack task management web application built with **Flask** and **MongoDB**. Supports user authentication and persistent to-do management — all organized with a modular Blueprint architecture.

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=flat-square&logo=flask&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-48.8%25-1572B6?style=flat-square&logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Environment Variables](#-environment-variables)
- [Running the App](#-running-the-app)
- [Deployment](#-deployment)
- [Contributing](#-contributing)

---

## ✨ Features

- 🔐 **User Authentication** — Secure register, login, and logout functionality
- ✅ **Task Management** — Create, view, update, and delete to-do items
- 💾 **Persistent Storage** — All data stored in MongoDB Atlas
- 🧱 **Modular Architecture** — Clean separation using Flask Blueprints
- 🌐 **Responsive UI** — Styled with custom CSS for a smooth experience
- ☁️ **Deployment Ready** — Includes `Procfile` for Heroku-style deployment

---

## 🛠 Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python, Flask 3.0.3     |
| Database   | MongoDB (via PyMongo)   |
| Frontend   | HTML5, CSS3             |
| Auth       | Werkzeug (password hashing) |
| Config     | python-dotenv           |
| Deploy     | Procfile (Heroku / Railway) |

---

## 📁 Project Structure

```
To-Do-App/
│
├── app/
│   ├── __init__.py          # App factory — creates Flask app, registers blueprints & DB
│   ├── models.py            # Database schema / data models
│   ├── routes/
│   │   ├── auth.py          # Authentication routes (register, login, logout)
│   │   └── tasks.py         # Task CRUD routes
│   ├── templates/           # Jinja2 HTML templates
│   └── static/              # CSS, JS, images
│
├── app.py                   # Application entry point
├── .env                     # Environment variables (not committed)
├── Procfile                 # Deployment process file
├── requirements.txt         # Python dependencies
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- MongoDB Atlas account (or local MongoDB instance)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nirvishsoni0401/To-Do-App.git
   cd To-Do-App
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (see below)

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
MONGO_URI=your_mongodb_connection_string
SECRET_KEY=your_secret_key_here
```

> ⚠️ Never commit your `.env` file. It's already in `.gitignore`.

---

## ▶️ Running the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

---

## ☁️ Deployment

This project includes a `Procfile` for deployment on platforms like **Heroku** or **Railway**.

```
web: python app.py
```

**Deploy to Heroku:**
```bash
heroku create your-app-name
heroku config:set MONGO_URI=your_mongo_uri SECRET_KEY=your_secret_key
git push heroku main
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Nirvish Soni**
- GitHub: [@nirvishsoni0401](https://github.com/nirvishsoni0401)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

> Made with ❤️ using Flask & MongoDB
