from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=200)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name
