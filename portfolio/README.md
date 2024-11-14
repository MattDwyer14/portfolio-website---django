Portfolio Website - Django

Introduction
Welcome to the Portfolio Website - Django project! This repository hosts a dynamic portfolio website developed using the Django framework. The site serves to exhibit projects, skills, and experiences, offering both aesthetic appeal and functional management capabilities through Django's admin interface.

Features
Responsive Design: Utilizes CSS, JavaScript, and Bootstrap for a clean, mobile-friendly layout.
Dynamic Content: Content management via Django admin for easy updates of projects, blog posts, and personal details.
Blog Section: Allows for the sharing of insights, tutorials, or experiences related to development.
Project Showcase: Detailed display of personal or professional projects.
Contact Form: Facilitates visitor inquiries through a managed form submission system.

Project Structure
Here's a brief overview of the directory structure:

portfolio_website/
manage.py: The Django command-line utility for administrative tasks.
portfolio_website/
settings.py: Configuration settings for the project.
urls.py: Defines URL patterns for the site.
projects/
admin.py: Configuration for the Django admin interface for managing projects.
forms.py: Contains forms for user interactions.
models.py: Defines the database models for Projects and Blog Posts.
views.py: Logic for handling requests and rendering responses.
urls.py: Project-specific URL configurations.
templates/
Project and blog templates, using Django's template language.
static/
CSS, JavaScript, and images used across the site.
blog/
Similar structure to projects for handling blog functionalities.
home/
Views and templates for the homepage.

Setup Instructions
Clone the Repository
bash
git clone https://github.com/MattDwyer14/portfolio-website---django.git
cd portfolio-website---django
Setup Virtual Environment
bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies
bash
pip install -r requirements.txt
Database Migration
bash
python manage.py migrate
Create Superuser for Admin Access
bash
python manage.py createsuperuser
Run the Development Server
bash
python manage.py runserver

Visit http://127.0.0.1:8000/ in your browser to see the site in action. Use /admin/ to manage content.

Customization
Adding Projects or Blog Posts: Log into the admin panel at /admin/ to add or edit content.
Styling: Modify the CSS files in the static directory to change the site's look.
Functionality: Extend models, views, and templates for additional features or sections.
