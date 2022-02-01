import email
from statistics import mode
from django.db import models

# Create your models here.

class Applications(models.Model):
    fio = models.CharField(max_length=150, default="Иванов Иван Иванович")
    email = models.CharField(max_length=255)
    birth = models.DateField()
    phone = models.CharField(max_length=20)
    education = models.CharField(max_length=255)
    desired_job = models.TextField()
    desired_start = models.DateField()
    desired_end = models.DateField()
    languages = models.CharField(max_length=255)
    volunteer_experience = models.TextField(blank=True,null=True)
    recommendations = models.TextField(blank=True, null=True)
    skills = models.TextField()
    volunteer_book = models.CharField(max_length=255, blank=True, null=True)
    why = models.CharField(max_length=255)
    video = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)


    def __str__(self):
        return self.fio
        