shell:
	docker compose run --rm django python manage.py shell_plus

makemigrations:
	docker compose run --rm django python manage.py makemigrations

migrate:
	docker compose run --rm django python manage.py migrate

makeandmigrate:
	docker compose run --rm django python manage.py makemigrations && docker compose run --rm django python manage.py migrate

rebuild:
	docker compose build --force

createsuperuser:
	docker compose run --rm django python manage.py createsuperuser

bash:
	docker compose run --rm django bash

reset_test:
	docker compose run --rm django python manage.py drop_test_database
