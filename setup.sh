pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py flush --noinput
python manage.py createsuperuser --noinput
python manage.py collectstatic --noinput