from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name + "," + self.major
        

# class 객체 등록하면 db가 자동으로 생성
# create table students(
#     name varchar2(100),
#     major varchar2(100),
#     age number(3),
    
# )
