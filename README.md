# Calculator
# 🧮 Django Calculator App

A simple calculator web app built using Django. It supports basic arithmetic operations and is styled with custom CSS. You can use it directly in your browser and it's deployed live on Render.

---

## 🚀 Live Demo

https://calculator-a4ys.onrender.com/  


---

## 📁 Project Structure

```
CalculatorProject/
├── calculator/           # Main Django app (views, templates)
│   ├── templates/
│   │   └── calculator.html    # Calculator UI
│   └── views.py
├── CalculatorProject/
│   ├── settings.py            # Django settings (whitenoise config, static setup)
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── Procfile               # Optional: Render deploy config
└── README.md
```

---

## ⚙️ Features

- Clean and responsive calculator UI
- Handles `+`, `-`, `*`, `/`, and decimal operations
- Real-time expression evaluation
- Error handling for invalid expressions
- Deployed to Render using Gunicorn + Whitenoise

---

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- Gunicorn
- Whitenoise
- HTML + CSS

---

## 🧑‍💻 Local Setup

### 1. Clone the repository

```bash
https://github.com/srisatyasai136/Calculator.git
cd Calculator
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python manage.py migrate
python manage.py runserver
```

Visit: http://127.0.0.1:8000

---

## ☁️ Deploying to Render

### Files you need:
- `Procfile` — tells Render to run Gunicorn
- `requirements.txt` — lists your Python packages
- `wsgi.py` — app entry point
- `settings.py` — must include static file setup and allowed hosts

### Steps:
1. Push code to GitHub
2. Go to https://render.com
3. Create new Web Service
4. Connect your GitHub repo
5. Set:
   - Build Command: pip install -r requirements.txt
   - Start Command: gunicorn CalculatorProject.wsgi

Done! Render will build and deploy your app.

---

## 📜 License

MIT License. Free to use, modify, and share.

---

## 🙋‍♂️ Author

**Sri Satya Sai Pasupuleti**  
📍 Hyderabad  
📧 srisatyasai136@gmail.com  
📞 6303496380  
[GitHub](https://github.com/srisatyasai136/)
