# Django Sales Application

Activate the virtual environment using - `pipenv shell`
To remove a virtual environment - `pipenv --rm`
To create a virtual environment using python - `python -m venv env && source env/bin/activate`
To create a virtual environment using virtualenv - `virtualenv env && source env/bin/active`
Install the dependencies using - `pipenv install`
Install the dependencies using requirements.txt - `pip install -r requirements/dev.txt`

To migrate the db changes  -`python manage.py migrate`
To create a super user - `python manage.py createsuperuser`
To create a new project - `django-admin startproject <project_name>`
To create a new app - `python manage.py startapp <app_name>`
To write dependencies to requirements.txt - `pipenv lock -r > requirements/prod.txt`
 `pipenv lock -r --dev-only > requirements/dev.txt` for dev dependencies
To make db migrations - `python manage.py makemigrations`
`python manage.py migrate`
To run the server - `python manage.py runserver`