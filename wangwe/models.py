from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='Projects/', blank=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField()
    technology = models.CharField(max_length=30)
    deploy = models.URLField(blank=True)
    source = models.URLField(blank=True)

    def __str__(self):
        return self.title
