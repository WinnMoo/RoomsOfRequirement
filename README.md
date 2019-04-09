# Rooms of Requirement for CECS 445

Room(s) of requirement is an app that identifies empty classrooms on the Cal State Long Beach campus to study in.

For CECS445

## Getting Started

This app is currently not ready for deployment: the user will have to install the dependencies needed and build the application stack from scratch.

## Dependencies

### Node.js

* Axios
* React
* Redux
* Redux Thunk

### Python

* Django
* Django Rest Framework
* bs4

## Deploying the servers

The Python server requires that you initialize a virtual environment inside the project directory.

```sh
pipenv shell
cd RoomsOfRequirement
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

And to actually draw the frontend, you must compile the Frontend project into a single .js file that Django can understand.

In another window...

```sh
npm i
npm prune
npm run dev
```

Note that most of the time, you only need to run the commands on the last line.

Type `localhost:8000` into your address bar of your favorite browser to see the results.
