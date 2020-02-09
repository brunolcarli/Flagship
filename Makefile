install_dev:
	pip install -r requirements.txt

run:
	python manage.py runserver 0.0.0.0:8000 --settings=star_destroyer.settings.common

migrate:
	python manage.py makemigrations --settings=star_destroyer.settings.common
	python manage.py migrate --settings=star_destroyer.settings.common
