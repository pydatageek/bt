There is no user UI, but just admin.

Please follow the process below to include dummy data.

1. start an environment with requirements
   e.g. pipenv install -r bt/requirements.txt
2. python manage.py migrate
3. python manage.py createsuperuser
4. python manage.py loaddata data.json

P.S: you may follow the process as the ordering defined or there may be problems with user related data

ABOUT:

- BT is a company's page, which organizes students' certification at universities.
- Students, enrolling to BT pick a qualification and one or more units within that qualification.
- Universities have certification programmes on one or more qualifications.

* Qualifications are at the center of the app!
  Employees, Universities, Students, Questions and Exams are all attended
  to a qualification.
* Sector > Qualification > Unit > Knowledge Statement (or Skill Statement)

* There is only one company and its settings.
* There are universities. Each university has one or more qualifications.
  Qualifications have units and those units have prices which are charged from
  students.

* Students are attended to qualifications (and some of their units)

* Each Knowledge Statement has more than 2 Knowledge Questions..
* Each Unit has more than 2 Skill Questions..
* Skill Questions doesnot have one to one match with Skill Statements, but Units.
