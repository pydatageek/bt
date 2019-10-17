please follow the process below

1. start an environment with requirements
    e.g. pipenv install -r bt/requirements.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py loaddata data.json

P.S: you may follow the process as the ordering defined or there may be problems with user related data
