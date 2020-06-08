# contact-form
## Output:
### Home page: 
  ![Home Page](/images/home_page.png)
### Create form page:
  ![Create form Page](/images/create_form.png)
### DashBoard:
  ![DashBoard Page](/images/dashboard.png)
### Details of each user:
  ![Details Page](/images/details.png)

## Task done:
  1. Created a webpage with a contact form consisting of:
     - Title select Field (Mr/Mrs/Ms)
     - Name Field
     - Email Field
     - Password Field (Password should be masked)
     - Phone Field
     - Address fields
     - Submit button
     - Date field is automatically saved
  2. Input validation, if invalid unable to submit.
  3. After submiting data redirect to view submitted details.
  4. View page to see all submitted data.
  5. MD5 Hashing of password.

## How to build:
```base
# Create virtual envorment
# * () means replace it with your name.
$ virtualenv (dir-name)
$ cd (dir-name)

# install django
$ pip install django

# INstall dependecy
$ pip install django-phonenumber-field
$ pip install phonenumbers

# Now clone repository in your local dir.
$ git clone https://github.com/ritikgarg655/contact-form.git

# Create user
$ cd contact-form
$ cd contact_form
$ python3 manage.py createsuperuser

#  Making migrations
$ python3 manage.py makemigrations
$ python3 manage.py migrate

# Run server
$ python3 manage.py runserver
```
## Open link: http://127.0.0.1:8000/contact_form/home
