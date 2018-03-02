# rename this file to "settings.py" for running tests: ./manage.py test

SECRET_KEY = 'very_secret'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'testdb',
    }
}

INSTALLED_APPS = [
    'swingtix.bookkeeper'
]
