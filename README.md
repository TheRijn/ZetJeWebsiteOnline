# Commerce

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
urlpatterns = [
    ...
    dbfiles_url(),
]
```

## `django-on-heroku`

https://pypi.org/project/django-on-heroku/

### `settings.py`
```python
SECRET_KEY = os.getenv('SECRET_KEY')
# Configure Django App for Heroku.
import django_on_heroku
django_on_heroku.settings(locals())
```

## Heroku

`Procfile`

    web: gunicorn -w 2 commerce.wsgi


git:

    git subtree push --prefix app heroku main

