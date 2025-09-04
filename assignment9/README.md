
# Django Blog Application


## Project Setup


1. **Create Django Project and App**
  ```bash
  django-admin startproject blog_project
  cd blog_project
  python manage.py startapp blog
````


2. **Define Models**


  In `blog/models.py`:


  ```python
  from django.db import models


  class Post(models.Model):
      title = models.CharField(max_length=200)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      category = models.CharField(max_length=100)


      def __str__(self):
          return self.title
  ```


3. **Run Migrations**


  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```


4. **Database Queries**


  In Django shell (`python manage.py shell`):


  ```python
  from blog.models import Post


  # Create instances
  Post.objects.create(title='First Post', content='Content here...', category='Tech')
  Post.objects.create(title='Second Post', content='More content...', category='Life')


  # Filter posts by category
  tech_posts = Post.objects.filter(category='Tech')
  print(tech_posts)
  ```


## Requirements


* Python 3.13.5
* Django 5.2.5


```




