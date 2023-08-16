# 🎉 DEMO Python Django

Django: Python web framework that streamlines backend development, encouraging efficient, secure, and scalable creation of dynamic websites and applications

![version](https://img.shields.io/badge/version-1.0-blue)
![rating](https://img.shields.io/badge/rating-★★★★★-yellow)
![uptime](https://img.shields.io/badge/uptime-100%25-brightgreen)

### 🚀 Setup

- Create Start Project

```
django-admin startproject app
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

```
python manage.py runserver
```