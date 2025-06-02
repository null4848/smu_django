from django.db import models

# Create your models here.
class Stuscore(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=100)
    kor = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    avg= models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.no}, {self.name, {self.total}}"