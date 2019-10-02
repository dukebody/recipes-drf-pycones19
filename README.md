Steps to perform BEFORE attending the tutorial session
=======================================================

0. Clone this repo:
```
git clone blablabla
```

1. Create a virtual environment for Python 3 and activate it.

Example with virtualenvwrapper:
```
mkvirtualenv -p python3 drf-recipes
```

See other options [here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

2. Install desired versions for Django and DRF:
```
pip install -r requirements.txt
```

3. Sync the database for first time:
```
python manage.py migrate
```

4. Create a superuser:
```
python manage.py createsuperuser --email admin@example.com --username admin
```

5. Start the development server:
```
python manage.py runserver
```

6. Open up the browser and login to the admin site at `http://127.0.0.1:8000/admin/`.