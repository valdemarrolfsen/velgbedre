web:python manage.py runserver --settings=velgbedre.settings
web: gunicorn velgbedre.wsgi --log-file -
heroku ps:scale web=1
