# Tasks-RESTful-APIs
Run project on local machine
To run the project on your local machine, please follow instructions:
```

$ mkdir .env //put it inside config directory
$ export DJANGO_READ_DOT_ENV_FILE=True
$ mkdir venv
$ virtualenv -p python3.6 venv/
$ source venv/bin/activate
$ python manage.py migrate --settings=config.settings.local
$ python manage.py runserver --settings=config.settings.local

```
