from django.db import models

class all_blog(models.Model):
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    date = models.DateTimeField(auto_now=False)
    image = models.ImageField(upload_to='media/blog/images/', blank=True)
    url = models.URLField(blank=True)

    
