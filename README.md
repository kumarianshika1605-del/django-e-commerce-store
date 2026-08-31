# 🛒 Django E-Commerce Store

A simple and responsive e-commerce web application developed using **Python and Django**.

This project demonstrates the basic functionality of an online shopping platform, including product listings, product details, shopping cart, user authentication, and order processing.

## 🚀 Features

- 🛍️ Product listing
- 🔎 Product details page
- 🛒 Add products to shopping cart
- ➕ Increase or decrease product quantity
- ❌ Remove products from cart
- 👤 User registration and login
- 🔐 User authentication
- 📦 Checkout and order processing
- 🧾 Order management
- 🗄️ Database storage for products, users, and orders
- ⚙️ Django Admin Panel for managing products and orders
- 📱 Responsive and user-friendly interface

## 🛠️ Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Django

### Database
- SQLite

### Development Tools
- Visual Studio Code
- Git
- GitHub

## 📂 Project Structure

```text
E-commerce/
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── store/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── manage.py
├── .gitignore
└── README.md
⚙️ Installation and Setup
1. Clone the repository
git clone https://github.com/YOUR-USERNAME/django-ecommerce-store.git
2. Open the project
cd django-ecommerce-store
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment
Windows
venv\Scripts\activate
macOS/Linux
source venv/bin/activate
5. Install Django
pip install django
6. Apply database migrations
python manage.py migrate
7. Create an admin account
python manage.py createsuperuser
Enter your username, email, and password when prompted.
8. Start the development server
python manage.py runserver
Open the application in your browser:
http://127.0.0.1:8000/
🔐 Django Admin
The Django Admin Panel can be accessed at:
http://127.0.0.1:8000/admin/

Conclusion
This Django-based e-commerce project successfully demonstrates the development of a basic online shopping platform using Python, Django, HTML, CSS, JavaScript, and SQLite. The application provides essential e-commerce features such as product listings, product details, shopping cart functionality, user authentication, checkout, and order processing.
The project helped in understanding how the frontend, backend, and database work together to create a complete web application. Django's Admin Panel also makes it easy to manage products, users, and orders.
Overall, this project provides a strong foundation for building a more advanced e-commerce platform in the future with features such as online payments, product reviews, search and filtering, wishlists, and order tracking.
