
from django.db import models

class Vos (models.Model):
    title = models.TextField()
    picture = models.ImageField(upload_to='vos/')

    def __str__(self):
        return self.title

class Geo (models.Model):
    title = models.TextField()
    picture = models.ImageField(upload_to='geo/')

    def __str__(self):
        return self.title

class Main (models.Model):
    title = models.TextField()
    pic1 = models.ImageField(upload_to='main/')
    pic2 = models.ImageField(upload_to='main/')
    pic3 = models.ImageField(upload_to='main/')

    def __str__(self):
        return self.title