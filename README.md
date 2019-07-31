# BACS
BACS - Builder's Account Checker System where end user can check their invested money's statement.

After setup the postgresql and python 3.7+ in your pc you can now clone or download this project.

After downloaded or cloned now you have to enter the inside of your project folder. You need to run some command to start your application.

First task: You need to create a database schema like 'bacs'. remember it,your username and password which is you stored when you install 
            postgresql,need to write into applications's settings.py file.
Second task: Go to your project folder and run some command in cmd
              commands are:
              1. pip3 install -r requirements.txt (this will install all the packages which are used in this project)
              2. python manage.py makemigrations ( this will create all table's schema)
              3. python manage.py migrate ( this will create all the tables)
              4. python manage runserver ( this will start the server and the application)
