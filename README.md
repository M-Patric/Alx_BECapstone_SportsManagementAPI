Sports Talent Management API

A Django REST Framework Project (ALX Backend Capstone)

Overview

The Sports Talent Management API is a backend system designed to manage athletes, training sessions, matches, and achievements.
It allows users (coaches, scouts, or admins) to register, authenticate, and manage all data through RESTful endpoints.

This API is secure, modular, and deployed live on Render.

Live API URL

Base URL: https://sportstalent.onrender.com
 
Features

User Authentication using Django REST Token Auth

Athlete Profiles — add, view, update, and delete athlete details

Training Sessions — track sessions, attendance, and feedback

Achievements — record and manage athlete awards

Matches — log and analyze match details and outcomes

 .env Configuration for security and portability

Modular App Structure for scalability

Fully Deployed on Render

Project Structure
Alx_BECapstone_SportsManagementAPI/
│
├── manage.py
├── requirements.txt
├── README.md
├── .env
│
├── sportstalent/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── users/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── athleteprofile/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── trainingsession/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── achievements/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
└── matches/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── tests.py

 Installation (Local Setup)
git clone https://github.com/<M-Patric>/Alx_BECapstone_SportsManagementAPI.git
cd Alx_BECapstone_SportsManagementAPI

Create Virtual Environment
py -m venv venv
source venv/Scripts/activate  # or venv\Scripts\activate

Install Dependencies
pip install -r requirements.txt

Create .env File
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

Apply Migrations
python manage.py migrate

Create Superuser
python manage.py createsuperuser

Run Server
python manage.py runserver

API Endpoints
Feature	Method	Endpoint	Description
Auth	POST	/api/users/register/	Register new user
Auth	POST	/api/users/login/	User login and token generation
Athletes	GET/POST	/api/athletes/	View or create athlete profiles
Athletes	PUT/DELETE	/api/athletes/<id>/	Update or delete profile
Training Sessions	GET/POST	/api/trainings/	Manage sessions
Achievements	GET/POST	/api/achievements/	Manage awards
Matches	GET/POST	/api/matches/	Manage match records
 Progress Report
 What I’ve Accomplished

Set up Django and Django REST Framework environment

Created five modular apps (users, athleteprofile, trainingsession, achievements, matches)

Configured token-based authentication

Implemented CRUD APIs for all models

Deployed API successfully on Render

Tested all endpoints using Postman

 Challenges Faced

Environment activation not reflecting initially (resolved by proper source venv/Scripts/activate)

Path confusion during migrations (fixed by keeping apps under project root)

Render build settings (resolved with correct gunicorn command and Procfile)

 What’s Next

Implement more complex query filters (e.g., filter training sessions by athlete or date)

Improve validation and authentication responses

Prepare for final capstone presentation

 Deployment on Render

Your Render configuration should look like this:

Build Command:

pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate


Start Command:

gunicorn sportstalent.wsgi


Environment Variables:

DEBUG=False
SECRET_KEY=<your_secret_key>
ALLOWED_HOSTS=your-render-url.onrender.com
