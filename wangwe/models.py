from django.db import models


class Feedback(models.Model):
    name = models.CharField(max_length=30, blank=False)
    email = models.EmailField()
    message = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return '%s - %s' % (self.name, self.email)


class Project(models.Model):
    title = models.CharField(max_length=60)
    image = models.ImageField(upload_to='projects/%Y/%m/', blank=False)
    description = models.TextField(blank=False)
    date = models.DateTimeField()
    technology = models.CharField(max_length=60)
    deploy = models.URLField(blank=True)
    source = models.URLField(blank=True)
    status = models.CharField(
        choices=(
            ('targeted', 'Targeted'),
            ('inprogress', 'In-Progress'),
            ('completed', 'Completed')
        ),
        max_length=10
    )

    def __str__(self):
        return self.title
