Users API
---------

To setup this application manually you should create virtualenv, 
setup your database according to project settings or overwrite them using local_settings
and run following commands:
```sh
$ pip install -r requirements.txt
$ ./manage.py migrate
$ ./manage.py runserver
```

Or you can setup this app using docker-compose simply typing
```sh
$ docker-compose up
```

To create users by console you may use django command ```populate``` 
with optional parameter ```-n``` to specify number of users to create.
```sh
$ ./manage.py populate -n 10
```

API Examples
------------

To create new user you should make POST request to http://localhost:8000/users/
with payload:
```json
{
  "name": "user first name",
  "surname": "user last name",
  "sex": "[0-1] | 0 - Male, 1 - Female",
  "age": "user age",
  "activities": [
    {"name": "activity name"},
    "..."
  ]
}
```

To search user by his activity you should make GET to http://localhost:8000/users/?activity=
and pass activity name through query params.

For more info about API implementation please visit http://localhost:8000/

Link to postman API collection: https://www.getpostman.com/collections/d4f897202ffc2ebee5c3

Also you can access users data via admin panel.
Default admin credentials is ```admin:admin```
