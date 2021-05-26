## CLI

### run server
- python3 ./manage.py runserver optional_number_port
### create an app
- django admin startapp name_of_the_app
### migrate apps
- python3 ./manage.py makemigrations
- python3 ./manage.py migrate

### create admin by cli
- python3 ./manage.py createsuperuser

## after set media directory

- python3 ./manage.py makemigrations blog
- python3 ./manage.py migrate --fake blog
- python3 ./manage.py migrate blog

### login admin
http://localhost:4000/admin/login/?next=/admin/

## packages
pip3 install django-bootstrap3