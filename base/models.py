from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    tableau = models.FloatField()
    sql = models.FloatField()
    r = models.FloatField()
    python = models.FloatField()
    big_data = models.FloatField()
    spss = models.FloatField()
    data_cleaning = models.FloatField()
    data_visualization = models.FloatField()
    modeling = models.FloatField()
    programming = models.FloatField()
    technical_average = models.FloatField()
    communication = models.FloatField()
    problem_solving = models.FloatField()
    critical_thinking = models.FloatField()
    leadership = models.FloatField()
    soft_average = models.FloatField()
    bootcamp_id = models.IntegerField()

def __str__(self):
        return str(self.student_id)