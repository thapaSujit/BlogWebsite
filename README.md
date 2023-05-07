# Django Tailwind Blog - A Developer Portfolio & Blog


![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## Introduction
**"Django Tailwind Blog"** is a developer blog and portfolio website built using **Django** and **Tailwind CSS**. It includes several pages (Home, About, Blog, Categories, and custom 404 pages). The project features a clean and modern design that is fully responsive and optimized for performance. It includes a powerful admin interface for managing the content, and is easy to customize and deploy to a production environment.

![django-tailwind-blog-for-developers](https://user-images.githubusercontent.com/106135144/227858936-d4cbcb44-9ff4-4729-b0f0-6ede931b99e0.png)

## Table of Content
  * [Introduction](#introduction)
  * [Installation](#installation)
  * [Technologies Used](#technologies-used)
  * [Features](#features)
  * [Pages](#pages)
  * [Acknowledgments](#Acknowledgments)
  * [License](#License)
  
## Installation
1. Clone the repository:
```
git clone git@github.com:thapaSujit/BlogWebsite.git
```
2. Navigate to the project directory:
```
cd `BlogWebsite`
```
3. Create and activate a new virtual environment:
```
python -m venv env
.\env\Scripts\activate
```
4. Install the project dependencies:
```
pip install -r requirements.txt
```
5. Add `tailwind` to your `INSTALLED_APPS` list in `settings.py`:
```python
INSTALLED_APPS = [
    # ...
    'tailwind',
    # ...
]
```
6. Run the Tailwind CSS configuration command:
```python
python manage.py tailwind init
```
7. Create the database tables:
```python
python manage.py migrate
```
8. Run the development server:
```python
python manage.py runserver
```

## Technologies used
1. HTML
2. CSS
3. JavaScript
4. Python

### Primary Modules used
1. Django==4.1.4
2. django-tailwind==3.4.0
3. whitenoise==6.3.0
4. psycopg2==2.9.5
5. django-tinymce==3.5.0

## Features
1. Responsive design using Tailwind CSS
2. Admin dashboard for managing blog posts and portfolio items
3. Contact form for sending messages to the site owner

## Pages
- `Home`: The landing page of the website, which displays a brief introduction and links to other pages.
- `About`: A page that provides information about the site owner, their background, and skills.
- `Blog`: A page that displays a list of blog posts in reverse chronological order, with links to individual post pages.
- `Blog Post`: A page that displays the content of a single blog post, including the title, author, date, and content.
- `Categories`: A page that displays a list of blog post categories, with links to filtered lists of posts for each category.
- `Custom 404 Pages`: Custom error pages that display when a user navigates to a non-existent page or encounters an error.


## Acknowledgments

This project was built upon the work of [Original Author](https://github.com/ashish-makes). I would like to express my gratitude for their initial implementation and inspiration.


## License

This project is licensed under the [MIT License](LICENSE). 

Based on initial work by [Original Author](https://github.com/ashish-makes). 

