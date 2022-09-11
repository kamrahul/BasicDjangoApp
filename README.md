# BasicDjangoApp
 Basic Django Blog management app

# Install PIP - Mac users

### Step1
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

### Step2
python3 get-pip.py

## Check pip version
pip3 --version

# Install pip env
sudo pip3 install pipenv


# Create virtual environment 
pipenv --python 3.8 install django==3.2

# Check files 
pipfile
pipfile.lock

# Activate virtual environemnt
pipenv shell


# Start a Django project
django-admin startproject BasicDjangoApp

# Run project 
Navigate to BasicDjangoApp

### Run command
python manage.py runserver

# Run Migration
python manage.py migrate


# Create super user
python manage.py createsuperuser

# Go to admin view by  /admin
localhost:8000/admin
