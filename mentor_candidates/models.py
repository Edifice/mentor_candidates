from __future__ import unicode_literals

from django.db import models

class Mentor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Opinion(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name
