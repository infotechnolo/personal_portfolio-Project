from django.db import models

class all_blog(models.Model):
    title = models.CharField(max_length=100)
    description= models.TextField(max_length=500)
    date = models.DateField(auto_now=False)
    image = models.ImageField(upload_to='media/blog/images/', blank=True)
    url = models.URLField(blank=True)

    
