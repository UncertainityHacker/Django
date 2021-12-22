# Django
Basics of Django

First Project created in Django to learn more and increase the competancy level.


## For Dynamic data
We can use dictionary to pass the data from backend to template file
We use model.py to define our class

## For Static data
we add the static folder in settings.py to access all the static files like css, js, bootstrap etc
for adding static files we use {% static '${static_file}' %} in the main html template instead to directly giving href and src

## Word Counter
Create a html in template to show the result, in views.py added the code to do processing, and routes added in urls.py

## Using POST method
By using POST method we are making our website more secure as the strings passed by user in forms is not shown in url, also by default in django csrf token is used which enhances the security

## Admin panel
Added Feature in admin.py and added data to db using default admin panel of django