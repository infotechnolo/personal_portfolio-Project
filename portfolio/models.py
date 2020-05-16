from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/portfolio/images/')
    url = models.URLField(blank=True) #this mean url is not a neccassry field, by default blank is fals(hence mandatory)

    def __str__(self):
        return self.title