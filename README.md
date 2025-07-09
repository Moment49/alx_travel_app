# 🚀 alx_travel_app API

Welcome to the **alx_travel_app** API! This project is a robust Django RESTful API designed for travel listings, featuring modern best practices such as environment-based configuration, CORS, Celery with RabbitMQ, and auto-generated Swagger documentation.

---

## 📝 Objective

- Set up a Django project with REST API capabilities.
- Securely configure a MySQL database using environment variables.
- Enable CORS for frontend-backend communication.
- Integrate Celery with RabbitMQ for background task processing.
- Provide interactive API documentation using Swagger (drf-yasg).

---

## 🛠️ Project Structure

```
alx_travel_app/
│
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── listings/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
│
├── requirements.txt
├── .env
└── manage.py
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/alx_travel_app.git
cd alx_travel_app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
# source venv/bin/activate  # On macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory with the following content:

```
DEBUG=True
SECRET_KEY=your-secret-key

DATABASE_ENGINE=django.db.backends.mysql
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=3306
```

> **Note:** Never commit your `.env` file to version control.

### 5. Set Up the Database

- Ensure MySQL is running and the database specified in `.env` exists.
- Run migrations:

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

---

## 🧩 Key Features & Configurations

### Django REST Framework

- Configured in `settings.py` for API development.
- Default filter backend: `django_filters.rest_framework.DjangoFilterBackend`.

### CORS

- Enabled via `django-cors-headers` for local development.
- Allowed origins set in `settings.py`.

### Celery & RabbitMQ

- Install and run RabbitMQ server locally.
- Celery configuration should be added to `settings.py` and a `celery.py` file.
- Example Celery command:

```bash
celery -A alx_travel_app worker --loglevel=info
```

### Swagger API Documentation

- Powered by `drf-yasg`.
- Visit [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) for interactive docs.

---

## 📚 Useful Commands

- **Run Tests:**  
  `python manage.py test`

- **Make Migrations:**  
  `python manage.py makemigrations`

- **Apply Migrations:**  
  `python manage.py migrate`

---

## 🗂️ Main Files

- `requirements.txt` – All dependencies.
- `alx_travel_app/settings.py` – Main configuration.
- `alx_travel_app/urls.py` – URL routing, including Swagger.
- `listings/` – Main app for travel listings.

---

## 🛡️ Security & Best Practices

- All sensitive data is managed via environment variables.
- CORS and CSRF settings are configured for safe API access.
- Swagger is enabled only in development.

---

## 📝 API Documentation

- **Swagger UI:** [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

---

## 🧑‍💻 Contributing

1. Fork the repo.
2. Create your feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙏 Acknowledgements

- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [drf-yasg (Swagger)](https://drf-yasg.readthedocs.io/)
- [Celery](https://docs.celeryq.dev/en/stable/)
- [RabbitMQ](https://www.rabbitmq.com/)

---

Happy coding! 🚀