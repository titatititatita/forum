## Forum project

This is a repository of an anonymous forum in which you can share your thougths without any signatures on topics you care about. Participate in other people's threads or create your own to start a discussion.

## Technologies used

- Python3
- Django
- Postgres13

## Running the application

To run the app use CLI and go to the /mysite directory, then run the following command:
```
$ docker run --name some-postgres -e POSTGRES_PASSWORD=root -d -p 5432:5432 postgres:13
$ python manage.py runserver
```
Now visit  http://127.0.0.1:8000/chat with your web browser