release: python manage.py makemigrations --no-input
release: python manage.py migrate --no-input
release: python manage.py createsuperuser --email admin@example.com --username admin --password shamirjamal

web: gunicorn closetpoint.wsgi

