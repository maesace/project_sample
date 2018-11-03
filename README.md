# Project sample

## Django Setup
1. Install Python 3. After installation, make sure that the current version of Python is correct.

        # Command
        python3 --version
        # Expected Output
        Python 3.6.3


2. Install Pip for Python 3. After installation, check the version using the following:

        # Command
        pip3 --version
        # Expected Output
        pip 9.0.1 from .../lib/python3.6/... (python 3.6)


3. Install Virtualenv for Python 3

        Note: You can skip this if you want to install the packages globally

        # Command
        pip3 install virtualenv

        # Creating a virtual environment
        virtualenv -p python3 venv

        # Activating the virtualenv venv
        source venv/bin/activate

        # Deactivating the virtualenv venv
        deactivate

4. Clone the repository

5. Install the local requirements

        # Command
        source venv/bin/activate
        pip install -r local.txt
        
6. Create a .env file which will contain your environment settings. Use env.example as reference.


7. Migrate the database

        python manage.py migrate

8. Create a superuser/admin

        python manage.py createsuperuser
        
9. Load mock data

        python manage.py loaddata project_sample/fixtures/mock_data.json

10. Collect static files

        python manage.py collectstatic --noinput -c

11. Run the server

        # Command
        python manage.py runserver
        
        
## Compile sass
        sass project_sample/web/static/sass/materialize.scss project_sample/web/static/css/materialize.css
