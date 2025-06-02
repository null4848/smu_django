from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.IntegerField(default=0)
    age= models.IntegerField(default=0)
    gender = models.CharField(max_length=30)
    
    def __str__(self):  # ✅ 올바른 메서드 이름
        return f"{self.name}, {self.major}"
