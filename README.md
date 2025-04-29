Project Overview
This project delivers a fully functional online store with product management, search, shopping cart, order history, theming, and user authentication. 
Django Project
 Under the hood it leverages Django’s MTV (Model‑Template‑View) architecture for clean separation of concerns. 
Django Project

Features
Dynamic Product Catalog: Users can browse and filter products by category, color, and size. 
GeeksforGeeks

Product Search: Implemented using Django Q objects to allow keyword and attribute‑based search. 
GitHub

Shopping Cart: “Add to Cart” functionality with session‑based storage for both anonymous and authenticated users. 
Stack Overflow

Order History: Registered users can view their past orders through a dedicated dashboard. 
Django Project

Theme Customization: Front‑end theming that lets users switch between light and dark modes dynamically. 
testdriven.io

Admin Interface: Customized Django Admin for product CRUD, filtering, and bulk operations. 
Earthly Lunar

User Authentication: Secure registration, login, logout, and session management using Django’s built‑in auth system. 
Django Project

Technical Highlights
Framework: Django (latest 4.x series) provides rapid development, built‑in security, and scalable structure. 
Django Project

Database: SQLite is used by default for development ease; fully supported by Django’s ORM. 
Stack Overflow

ORM: Django’s ORM abstracts SQL into Pythonic models and querysets for data access. 
GeeksforGeeks

Templating: Leveraged Django Templates to render dynamic HTML with context data. 
Django Project

Routing: Clean URL patterns defined in urls.py map paths to views. 
testdriven.io

Admin Customization: Extended the admin site via admin.py—added filters, search fields, and custom list displays. 
Earthly Lunar

Prerequisites
Python: Version 3.8 or higher. 
docs.python-guide.org

pip: Package installer for Python. 
Learn R, Python & Data Science Online

virtualenv or pipenv: Recommended to isolate dependencies. 
docs.python-guide.org

Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/abrar898/Ecommerce-Django.git
GitHub

Navigate into the project folder

bash
Copy
Edit
cd Ecommerce-Django
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Learn R, Python & Data Science Online

Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Stack Overflow

Database Setup
Apply migrations

bash
Copy
Edit
python manage.py migrate
Django Project

(Optional) Load sample data

bash
Copy
Edit
python manage.py loaddata fixtures/sample_products.json
Running the Project
Start the development server:

bash
Copy
Edit
python manage.py runserver
Then visit http://127.0.0.1:8000/ in your browser. 
W3Schools.com

Usage
Admin Access:
Create a superuser and log in at /admin/:

bash
Copy
Edit
python manage.py createsuperuser
Django Project

Changing Themes:
Use the theme toggle in the site header to switch between light and dark modes. 
testdriven.io

Contributing
Contributions are welcome! Please fork the repo, create a feature branch, and open a pull request. 
