from django.db import models




###    We create a model called HomeAds to save the extracted data to the database. 
##     where "no" is unique, preventing re-saving of each retrieved data


class HomeAds(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField()
    price = models.CharField(max_length=50, null=False, blank=False)
    currency = models.CharField(max_length=4)
    square_price = models.CharField(max_length=30, null=True, blank=True)
    category = models.CharField(max_length=50, null=False, blank=False)
    floor = models.CharField(max_length=10, null=False, blank=False)
    area = models.CharField(max_length=50, null=False, blank=False)
    rooms = models.CharField(max_length=50, null=False, blank=False)
    buy_or_rent = models.CharField(max_length=50)
    no = models.CharField(max_length=50, null=False, blank=False, unique=True)
    image_url = models.TextField()
    
    def __str__(self):
        return self.title + " " + self.price + " " + self.currency

    


