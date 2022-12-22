admin:
	python ./manage.py createsuperuser

migrate:
	python ./manage.py makemigrations
	python ./manage.py migrate

run:
	python ./manage.py runserver

freeze:
	pip freeze >requirements.txt
