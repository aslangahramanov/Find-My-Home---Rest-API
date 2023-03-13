from django.db import models

# Create your models here.



class OnSaleHouse(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    currency = models.CharField(max_length=4)
    square_price = models.CharField(max_length=30)
    category = models.CharField(max_length=50, null=False, blank=False)
    floor = models.CharField(max_length=10, null=False, blank=False)
    area = models.CharField(max_length=50, null=False, blank=False)
    rooms = models.CharField(max_length=50, null=False, blank=False)
    title_deed = models.BooleanField(default=True, null=True, blank=True)
    mortgage = models.BooleanField(default=True, null=True, blank=True)
    repair = models.BooleanField(default=True, null=True, blank=True)
    residential = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    



class RentalHouse(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.IntegerField(null=False, blank=False)
    currency = models.CharField(max_length=4)
    category = models.CharField(max_length=50, null=False, blank=False)
    floor = models.CharField(max_length=10, null=False, blank=False)
    area = models.CharField(max_length=50, null=False, blank=False)
    rooms = models.CharField(max_length=50, null=False, blank=False)
    repair = models.BooleanField(default=True, null=True, blank=True)
    residential = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    

