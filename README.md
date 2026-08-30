## 1. Install django

`pip install Django`

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

If you deleted the databases or changed it should apply the migration or perply won't work correctly. apply with below code:

```code
python manage.py migrate
```

## 4. N.B

the files below are required to understand:
**manage.py** used to interact with django<br>
**settings.py** the core of django wich include all necessary things like authentications, templates, databases ...<br>
**urls** which tells django which pages urls should use and where.<br>
