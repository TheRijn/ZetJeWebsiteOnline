# Commerce

## `requirements.txt`

```
Gunicorn  # Webserver
Django
django-on-heroku
django-dbfiles  # Only when using file uploads
Pillow  # Only when using ImageField
```


## django-dbfiles

https://pypi.org/project/django-dbfiles/


### `settings.py`

```python
# Add 'dbfiles' to INSTALLED_APPS
INSTALLED_APPS = [
    'dbfiles',
]

# Optionally set DEFAULT_FILE_STORAGE
DEFAULT_FILE_STORAGE = 'dbfiles.storage.DBStorage'

# Choose a root url for uploaded files
MEDIA_URL = '/media/'
```


### `urls.py`
```python
from dbfiles.urls import dbfiles_url

urlpatterns = [
    ...
    dbfiles_url(),
]
```


## `django-on-heroku`

https://pypi.org/project/django-on-heroku/


### `settings.py`

At the very bottom:
```python
# Configure Django App for Heroku.
import django_on_heroku
django_on_heroku.settings(locals())
```


## Heroku

https://devcenter.heroku.com/articles/heroku-cli

`Procfile`

    release: python ./app/manage.py migrate
    web: gunicorn --chdir ./app -w 2 commerce.wsgi


## Create a secret key

    python3 -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"


## Create superuser

    $ heroku run bash

A heroku shell opens

    $ python manage.py createsuperuser
