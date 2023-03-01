# BlissFeed API (Django REST Framework) - [Live link](https://blissfeed-drf.herokuapp.com/)

Welcome to BlissFeed API, powered by Django REST Framework! This API is designed to provide seamless communication between the frontend social media web app called BlissFeed and it's backend server. With full CRUD functionality.


![alt text](../blissfeed-drf-api/images/Screenshot%202023-03-01%20at%2001.24.52.png "")

# Data Model

The backend API application is built with [Django REST framework](https://www.django-rest-framework.org/).

## ERD
- TEST
***
## User model
- TEST
***
## Post model
- TEST
***
## Category model
- TEST
***


## Database

- PostgreSQL is used in production to store all data.
- Database is hosted on [ElephantSQL](https://www.elephantsql.com/).

# User Stories

For the backend part of this project, there is only one user story:

- As an admin, I want to have full CRUD(create, edit, delete) functionality for all the users, posts, comments and likes, so that I can for example delete malicious content from the page.

# Technologies

## Languages used

- [Python](https://www.python.org/)

## Workspace

### Gitpod
[GitPod](https://gitpod.io/)
- GitPod was used as the main IDE workspace to build this API.

## Version Control

### Git
[Git](https://git-scm.com/)
- Git was used as a version control system that allowed me to keep track of changes in my code over time.

### GitHub
[GitHub](https://github.com/) 
- GitHub stores the code for this project after being pushed from Git.

## ERD

### ?

## Development

### Django Rest Framework
- [Django REST Framework](https://www.django-rest-framework.org/)
used to build the backend API.

### Django AllAuth
- [Django AllAuth](https://django-allauth.readthedocs.io/en/latest/index.html)
used for authentication of users.

## Hosting/Database

### Heroku
- [Heroku](https://id.heroku.com/login)
is used to host the application.

### Gunicorn
- [Gunicorn](https://gunicorn.org/)
used for deploying the application to Heroku.

### Cloudinary
- [Cloudinary](https://cloudinary.com/)
is used to store and host the media files.

### Pillow 
- [Pillow](https://pillow.readthedocs.io/en/stable/)
is used for image processing and validation.

### Psycopg2
- [psycopg2](https://www.psycopg.org/docs/)
is used for PostgreSQL Python adaption.

### PostgreSQL
- [PostgreSQL](https://www.postgresql.org/)
is used for the production database.

### PyJWT
- [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
PyJWT for encode and decode JSON Web Tokens.

# Testing

## Pep8
- PEP8 shows no errors, some errors were found in the settings.py - no need to fix.

## Manual testing of user stories

- As an admin, I want to have full CRUD(create, edit, delete) functionality for all the users, posts, comments and likes, so that I can for example delete malicious content from the page.

| Test       | Action            | Expected Result               | Pass |
| ---------- | ---------------- | --------------------------- | ---- |
| Users     | Create, edit, delete   | A user can be created, edited or deleted.   | ✓    |
| Users     | Update permissions  | The user permissions can be updated.      | ✓    |
| Profiles   | Create, edit, delete | A profile can be created, edited or deleted.  | ✓    |
| Posts  | Create, edit, delete       | A post can be created, edited or deleted.        | ✓    |
| Comments   | Create, edit, delete | A comment can be created, edited or deleted.   | ✓    |
| Likes   | Create, edit, delete | A like can be created, edited or deleted.   | ✓    |

## Bugs

- Broken CSS for the admin panel, it seems to be a DRF bug.

# Deployment

1.  Clone [this repository](https://github.com/Aspen92/blissfeed-drf-api).
2.  In your IDE, connect to your repo, then enter this command in the terminal:
        
        pip install -r requirements.txt

- Make sure your INSTALLED_APPS in settings.py look like this:

        INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'cloudinary_storage',
        'django.contrib.staticfiles',
        'cloudinary',
        'rest_framework',
        'django_filters',
        'rest_framework.authtoken',
        'dj_rest_auth',
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'dj_rest_auth.registration',
        'corsheaders',
        'profiles',
        'posts',
        'comments',
        'likes',
        'followers',
        'categories',
        ]

3. In you terminal, enter these commands in the terminal:

        python manage.py makemigrations
        python manage.py migrate

4.  Git add, commit and push all changes to your repo.
5.  Create or log in to an account on Heroku.
6.  Create a new app on Heroku.
7.  Open your app on Heroku, go to Resources, Add-ons and search for PostgreSQL, then add it.
8.  In the Deploy tab on Heroku, go to Deployment method and add your GitHub repository.
9.  In the Deploy tab on Heroku, go to Manual deploy and select deploy branch for early deployment.
10. Create or log in to an account on Cloudinary.
11. Copy your API Environment Variable.
12. Go back to Heroku, Settings and click on Reveal Config Vars.
13. Add these variables to your config vars. PostgreSQL DATABASE_URL should already be there.
    - ALLOWED_HOST | your_deployed_api_url
    - CLIENT_ORIGIN | your_deployed_frontend_url
    - CLIENT_ORIGIN_DEV | your_local_server_url
    - CLOUDINARY_URL | your_api_variable
    - SECRET_KEY | your_choice ([Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/))
    - DISABLE_COLLECTSTATIC | 1
14. Create an env.py in the root directory, add it to .gitignore and add these lines at the top

        import os

        os.environ["SECRET_KEY"] = "your secret_key here"
        os.environ["CLOUDINARY_URL"] = "cloudinary url here"
        os.environ['DEV'] = '1'

15. In settings.py, update the CORS_ALLOWED_ORIGIN_REGEXES variable to match your local server url.

        if 'CLIENT_ORIGIN_DEV' in os.environ:
            extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
            CORS_ALLOWED_ORIGIN_REGEXES = [
                rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
            ]

16. Create a superuser for your site:

        python manage.py createsuperuser

17. To run your app locally, enter this command in your terminal:
        python manage.py runserver

# Credits

## Code

- This API was built using Django REST Framework. The source code is from Code Institute's Django REST API walkthrough project [GitHub](https://github.com/Code-Institute-Solutions/drf-api). I decided to use the base of whole project on this API since it was a great fit for the application I had planned and it provides a great foundation to expand upon.

## Acknowledgements

- My best friend Lucas Holm for helping me solve some problems that i stumbled upon during this project.
- [Code Institute](https://codeinstitute.net/) tutors (Sean & Oisin) for help with various issues.
- [Stack Overflow](https://stackoverflow.com/) for tips, tricks and solutions to fix difficult errors.