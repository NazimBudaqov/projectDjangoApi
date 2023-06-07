from django.db import models

# Create your models here.
class Student(models.Model):
    studentID = models.AutoField(primary_key=True)
    python = models.FloatField(max_length=200)
