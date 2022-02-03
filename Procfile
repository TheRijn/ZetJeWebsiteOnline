release: python ./app/manage.py migrate
web: gunicorn --chdir ./app -w 2 commerce.wsgi