
# Prime-session backend setup

postgresql.txt 
Install:

sudo yum install postgresql-server
cp -rp /var/lib/pgsql /space/postgresql
sudo postgresql-setup initdb
sudo systemctl enable postgresql-service
sudo systemctl start postgresql

sudo -u postgres psql
postgres=# CREATE DATABASE prime;
CREATE DATABASE
postgres=# CREATE USER primesys WITH PASSWORD 'xxx';
CREATE ROLE
postgres=# ALTER ROLE primesys SET client_encoding TO 'utf8';
ALTER ROLE
postgres=# ALTER ROLE primesys SET default_transaction_isolation TO 'read committed';
ALTER ROLE
postgres=# GRANT ALL PRIVILEGES ON DATABASE prime TO primesys;
GRANT
postgres=# \q

sudo -u postgres createuser xxx

vi /space/postgresql/data/pg_hba.conf
  set to peer
  sudo systemctl restart postgresql
then
  sudo -u postgres psql
  ALTER USER postgres PASSWORD 'xxx';
vi again
  set to md5
  restart

psql --username=primesys   (pass xxx)
psql --username=postgres   (pass xxx)


cat *django*
sudo pip install virtualenv

cd /space
mkdir django
cd django
mkdir prime
cd prime

virtualenv venv

source venv/bin/activate

pip install django psycopg2

django-admin.py startproject prime .

cd prime

vi settings.py
ALLOWED_HOSTS = [ 'vs-dev001.maximusbchealth.local', '127.0.0.1' ]
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prime',
        'USER': 'xxx',
        'PASSWORD': 'xxx',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

cd /space/django/prime
source venv/bin/activate
-- from now any packages we install with pip will go here

-- to deactivate (go back to standard python):
deactivate

-- to start the server
cd /space/django/prime
pything manage.py runserver
-- now can connector to http://127.0.0.1:8000

-- to create a sample app
cd /space/django/prime
django-admin.py startproject prime .  (done before)
-- edit settings.py
      settings.py : settings
      settings_secret.py : password file (not in github)
      urls.py : url to view mappings
      wsgi.py : comm from app to web server (boilerplate)
      manage.py : create apps, work with dbs, start web server

-- to create the prime-data application that lives inside prime
python manage.py startapp prime-data
python manage.py startapp prime-session
      migrations : files to update the DB as we modify the model
      __init__.py : empty file to make folder python.

-- edit prime/settings.py and add entries that were in
      prime_data/apps.py and prime_session/apps.py, these are:
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'prime_data.apps.PrimeDataConfig',
    'prime_session.apps.PrimeSessionConfig',
]

-- in prime/settings.py:
    TIME_ZONE = 'America/Vancouver'
    SECRET_KEY : for website security, read from environment in PROD
    DEBUG : debugging logs on error instead of HTTP status code.  Set to False in PROD

-- set the URLs
    in prime/urls.py

