# 🎉 DEMO Python Django

Django: Python web framework that streamlines backend development, encouraging efficient, secure, and scalable creation of dynamic websites and applications

![version](https://img.shields.io/badge/version-1.0-blue)
![rating](https://img.shields.io/badge/rating-★★★★★-yellow)
![uptime](https://img.shields.io/badge/uptime-100%25-brightgreen)

### ⭐ Features

- [CKEditor](https://www.pycodemates.com/2022/03/integrate-ckeditor-to-django-admin-and-form-fields.html)
- [Import and Export](https://django-import-export.readthedocs.io/en/latest/index.html)
- [Search](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
- [Pagination](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)
- [Logs](https://www.airplane.dev/blog/django-application-monitoring)
- [Model Meta Class](https://docs.djangoproject.com/en/4.2/ref/models/options/)
- [SSL Server](https://github.com/teddziuba/django-sslserver)
- [UUID Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
- [Slug Field](https://docs.djangoproject.com/en/4.2/ref/models/fields/)
- [Image Field](https://docs.djangoproject.com/en/4.2/topics/files/)
- [File Field](https://docs.djangoproject.com/en/4.2/topics/files/)
- [Random File Name](https://stackoverflow.com/questions/2673647/enforce-unique-upload-file-names-using-django)
- [Show Image](https://dev.to/vijaysoni007/how-to-show-images-of-the-model-in-django-admin-5hk4)
- [Show Many Field](https://stackoverflow.com/questions/18108521/how-to-show-a-many-to-many-field-with-list-display-in-django-admin)
- [Deploy](https://docs.djangoproject.com/en/4.2/howto/deployment/)
- [Daphne ASGI](https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/daphne/)
- [Admin Interface](https://testdriven.io/blog/customize-django-admin/)

### 🚀 Setup

- Create Start Project

```
django-admin startproject core
```

- Create App

```
python manage.py startapp module
```

- Make Migration

```
python manage.py makemigrations
```

- Show Migration

```
python manage.py showmigrations
```

- Migrate

```
python manage.py migrate
```

- Create User

```
python manage.py createsuperuser
```

- Create Static Folder

```
python manage.py collectstatic
```

### 🔑 Configuration

- Change Timezone

```
TIME_ZONE = 'Asia/Bangkok'
```

- Allow Host

```
ALLOWED_HOSTS = ['127.0.0.1']
```

- Disable Debug

```
DEBUG = False
```

### 🏆 Run

- [http://localhost:8000/admin](http://localhost:8000/admin) username : `admin` password : `admin`
- [https://localhost:8000/admin](https://localhost:8000/admin) username : `admin` password : `admin`

```
python manage.py runserver
python manage.py runsslserver
python manage.py runsslserver --certificate ../certs/localhost.crt --key ../certs/localhost.key
```

### 🧩 Production

```
python manage.py check --deploy
daphne core.asgi:application
```

### 💣 Remove App

1. Remove App from `INSTALLED_APPS` in `settings.py`
2. Delete App's Database Tables
```
python manage.py makemigrations -n drop_all_tables module
```
3. Delete App's Files
4. Remove App's URLs in `urls.py`
5. Clear Cached Files
6. Check for Dependencies
7. Test Your Project