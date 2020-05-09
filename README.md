# contact-form

## How to use:
```base
# Create virtual envorment
$ virtualenv (dir-name)

# install django
$ pip install django

# INstall dependecy
$ pip install django-phonenumber-field
$ pip install phonenumbers

# Now clone repository in your local dir.
$ git clone https://github.com/ritikgarg655/contact-form.git

# Create user
$ python3 manage.py createsuperuser (user_name)

#  Making migrations
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# Run server
$ python3 manage.py runserver
```

## Open link: http://127.0.0.1:8000/contact_form/home

# Output:
## Home page: 
  ![Home Page](/images/home_page.png)
## Create form page:
  ![Create form Page](/images/create_form.png)
## DashBoard:
  ![DashBoard Page](/images/dashboard.png)
## Details of each user:
  ![Details Page](/images/details.png)
