# Online Library System (Django Project)

Django web application to manage an online library system where admins can manage books, authors, and their borrow records. The application should allow admins to add books, authors, and assign books to authors. Additionally, admins should be able to export the library data to an Excel sheet.

---

# Features

- Add, view, and manage Authors, Books, and Borrow Records
- Export all data to an Excel file with separate sheets
- Clean, simple UI with form validation

---

1. create a Virtual envirment

-python -m venv venv
-venv\Scripts\activate

2- install Django

-pip install djago

3-install the library

-openpyxl

4- Start project

-django-admin startproject library_system
-cd library_system

5-Start app

-pyhton manage.py startapp

6- Create Super user

-python manage.py createsuperuser

7-Apply Migrations

-python manage.py makemigrations
python manage.py migrate

8-Run the Development Server

-python manage.py runserver

Open your browser and go to:-
http://127.0.0.1:8000/

Example:-

http://127.0.0.1:8000/author/
http://127.0.0.1:8000/book/
http://127.0.0.1:8000/borrow/
http://127.0.0.1:8000/export/
