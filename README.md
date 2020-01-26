There is no frontend, just backend.

Please follow the process below to include dummy data.

1. start an environment with requirements
   e.g. pipenv install -r bt/requirements.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py loaddata data.json

P.S: you may follow the process as the ordering defined or there may be problems with user related data

SUMMARY:
Sector > Qualification > Unit > Knowledge Statement (or Skill Statement)

Students are attended to qualifications (and units)

Each Knowledge Statement has more than 2 Knowledge Questions..
Each Unit has more than 2 Skill Questions..
