from django.db import models

# Create your models here.

class Bootcamp(models.Model):
    bootcamp_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.bootcamp_id)

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    tableau = models.FloatField(default=0)
    sql = models.FloatField(default=0)
    r = models.FloatField(default=0)
    python = models.FloatField(default=0)
    big_data = models.FloatField(default=0)
    spss = models.FloatField(default=0)
    data_cleaning = models.FloatField(default=0)
    data_visualization = models.FloatField(default=0)
    modeling = models.FloatField(default=0)
    programming = models.FloatField(default=0)
    technical_average = models.FloatField(default=0)
    communication = models.FloatField(default=0)
    problem_solving = models.FloatField(default=0)
    critical_thinking = models.FloatField(default=0)
    leadership = models.FloatField(default=0)
    soft_average = models.FloatField(default=0)
    bootcamp = models.ForeignKey(Bootcamp, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.student_id)