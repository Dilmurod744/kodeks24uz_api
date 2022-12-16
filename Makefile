admin:
	./manage.py createsuperuser

migrate:
	./manage.py makemigrations
	./manage.py migrate

run:
	./manage.py runnserver

requirements:
	pip freeze >requirements.txt
