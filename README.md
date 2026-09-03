## 1. Install django

```code
pip install Django
```

## 2. Create new Project

```code
django-admin startproject NAME_THE_PROJECT
```

Django will create `NAME_THE_PROJECT` folder, with subfolders inside it

## 3. Running the Project

```code
python manage.py runserver
```

Django will create new sqlite database called **db.sqlite3**

## 4. migration

If you deleted the databases or changed it should apply the migration or perply won't work correctly. apply with below command:

```code
python manage.py migrate
```

## 4. N.B

### Please understand the following notices:

\
**\_\_init\_\_.py** tells python to consider the folder django_tuto
\
**manage.py** used to interact with django
\
**settings.py** the core of django wich include all necessary things like authentications, templates, databases ...
\
**urls** which tells django which pages urls should use and where.

### For each app you should create these files which necessary:

**models** is the database
\
**views** the leader of the app
\
**templates** this folder you will be create for all website design (front-end)
\
**urls** another file should be create for each app created to specify the urls and pages

## 5. Adding an APP

To create new app use the following command

```code
python manage.py startapp APP_NAME
```

### The command will create multi files and you have to take as considerations all of these:

**admin.py** each app should has admin web page which you control your website.
\
**models.py** the data you wright to insert into the database
\
**views.py** this control to show all of your things shown on your app
\

### N.B

Every time you create a new app you should register inside settings.py in **INSTALLED_APPS**
e.g: "pages.apps.PagesConfig".
Here you are aiming for the class inside apps.py that created when you added new app earlier
