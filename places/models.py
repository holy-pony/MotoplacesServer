from django.db import models


class PlaceType(models.Model):
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Shop(models.Model):
    shop_title = models.CharField(max_length=100)
    shop_website = models.CharField(max_length=200)
    shop_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.shop_title


class Place(models.Model):
    place_title = models.CharField(max_length=200)
    place_lat = models.FloatField()
    place_lng = models.FloatField()
    pub_date = models.DateTimeField('date published')
    place_type = models.ManyToManyField(PlaceType)
    place_discription = models.CharField(max_length=200, blank=True, null=True)
    place_address = models.CharField(max_length=200, blank=True, null=True)
    place_shop = models.ForeignKey(Shop , blank=True, null=True)

    def __str__(self):
        return self.place_title
