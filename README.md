# Djando test app

## How to run it

- Make sure you have Docker installed.
- Run `docker-compose up` to run the DB and Web servers
- In another Bash/Terminal session, run `docker-compose run web python manage.py createsuperuser` to create an admin user
- If you get an error message from Docker, run `eval "$(docker-machine env default)"`
