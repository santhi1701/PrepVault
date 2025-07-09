# Prepvault 🎯

**Smarter Interview Preparation for Students & Freshers**

Prepvault is a Django-based platform that helps students prepare for technical interviews with quizzes, resources, and performance dashboards — all in one place.

---

## 🌐 Live Demo

🔗 [https://prepvault-q3qz.onrender.com](https://prepvault-q3qz.onrender.com)

---

## 🚀 Features

- ✅ Register/Login/Logout system
- ✅ Topic-wise quiz bank (Python, Aptitude, DBMS, etc.)
- ✅ Personalized performance dashboard
- ✅ Company-wise interview resources
- ✅ Admin panel for managing users/questions
- ✅ Role-based access (admin, staff, student)
- ✅ Deployed on Render (production ready)

---

## 🛠 Tech Stack

| Layer        | Technology                        |
|--------------|------------------------------------|
| Framework    | Django 5.2                         |
| Language     | Python 3                           |
| Frontend     | HTML5, Bootstrap 5, CSS            |
| Auth         | Django Authentication              |
| Database     | SQLite (locally), Render DB ready  |
| Deployment   | Render Cloud Hosting               |

---
## 📁 Project Structure
career_companion/
│
├── main/ # Core Django app
│ ├── migrations/ # DB migrations
│ ├── static/ # Static files (CSS, JS, images)
│ ├── templates/ # HTML templates
│ ├── admin.py # Admin config
│ ├── models.py # Database models
│ ├── views.py # View functions
│ └── urls.py # App-specific routes
│
├── career_companion/ # Project settings
│ ├── init.py
│ ├── settings.py # Main settings file
│ ├── urls.py # Main URL config
│ └── wsgi.py # WSGI for deployment
│
├── db.sqlite3 # SQLite database
├── manage.py # Django CLI entry point
├── requirements.txt # Python package list
└── README.md # Project README




