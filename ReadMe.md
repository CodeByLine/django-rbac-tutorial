Following tutorial: "Setting up Django REST API with custom user model and tests"

https://dev.to/ksaaskil/setting-up-django-rest-api-with-custom-user-model-and-tests-5b8f


$ mkdir django-rbac && cd django-rbac
$ pyenv virtualenv 3.8.1 django-rbac-3.8.1
$ pyenv local django-rbac.3.8.1

$ printf "django==3.1.7\n" > requirements.txt
$ pip install -r requirements.txt
$ django-admin startproject rbac .

$ python manage.py startapp core
$ mv core rbac/

# Rename app from 'core' to 'rbac.core'
class CoreConfig(AppConfig):
    name = 'rbac.core'