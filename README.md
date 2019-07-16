# DjangoAngularJWT
This project is the example of the JWT usage with DRF and Angular In frontend/angular, git submodule and it's the angular part.
For quick start, please see the Getting Started section. I made simple user auth, user register, login and post microblog.

## Packages
* Django 2.1.1
* DjangoRestFramework
* DjangoCorsHeader
* DjangoRestFramework-simpleJWT
* Angular 8.1.1
* Angular-jwt
* Others

## Getting Started
1) Clone the project (You should use --recursive to download submodules, for this project it's angular project)
```
$ git clone --recursive https://github.com/MarlonJD/DjangoAngularJWT.git
```
2) Go to project folder
```
$ cd DjangoAngularJWT
```
3) Create Python virtual env, (wait a little bit)
```
$ python -m venv venv
```
4) Activate virtual env for python. (you should see (venv) prefix on your terminal)
```
$ source venv/bin/activate
```
5) Install the packages needs.
```
$ pip install -r requirements.txt
```
6) Migrate the Django for database etc.
```
$ python manage.py migrate
```
7) And Django is ready to use. Start server on 8000 port. You can see the website on http://127.0.0.1:8000
```
$ python manage.py runserver
```


## Angular the Front-Side
Please see the [Angular Project](https://github.com/MarlonJD/AngularJWT/).
