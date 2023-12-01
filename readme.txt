        startapp
python3.7>      old now work
    ### python manage.py startapp advertisements
new:
    py -m django startapp advertisements



python manage.py migrate now work
edit file setting.py:
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

example:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


	startapp 2
django-admin startproject base .
python .\manage.py runserver



        Интернационализация LINUX (windows gettext)
1.  python manage.py makemessages -l ru
2.  python manage.py compilemessages