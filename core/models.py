from django.db import models


class Projects(models.Model):
    name = models.CharField(max_length=40, primary_key=True)
    category = models.CharField(max_length=50)
    url = models.URLField()
    image = models.ImageField(upload_to='media/projects')
    rating = models.IntegerField()
    date = models.DateTimeField(auto_now=True)
