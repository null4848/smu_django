from django.db import models

# Create your models here.
class Product(models.Model):
    pno = models.AutoField(primary_key=True),
    title = models.CharField(max_length=1000),
    main_category = models.CharField(max_length=200),
    sub_category2 = models.CharField(max_length=200),
    origin = models.CharField(max_length=100),
    weight = models.IntegerField(default=0),
    price = models.IntegerField(default=0),
    dcprice = models.IntegerField(default=0),
    stock = models.IntegerField(default=0),
    main_image = models.ImageField()
    sub_image1 = models.ImageField()
    sub_image2 = models.ImageField()
    create_date = models.DateField()
    update_date = models.DateField()
    