from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name  # 또는 원하는 출력 형식

