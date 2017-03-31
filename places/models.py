from django.db import models


class PlaceType(models.Model):
    type = models.CharField(max_length=16)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Location(models.Model):
    location_title = models.CharField(max_length=200)
    location_lat = models.FloatField()
    location_lng = models.FloatField()

    def __str__(self):
        return self.location_title


class Shop(models.Model):
    shop_title = models.CharField(max_length=100)
    shop_website = models.CharField(max_length=200)
    shop_phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.shop_title


class Place(models.Model):
    place_title = models.CharField(max_length=200)
    place_position = models.OneToOneField(Location, null=True)
    pub_date = models.DateTimeField('date published')
    place_type = models.ManyToManyField(PlaceType, related_name="places_type_rel")
    place_discription = models.CharField(max_length=200, blank=True, null=True)
    place_address = models.CharField(max_length=200, blank=True, null=True)
    place_shop = models.ForeignKey(Shop, blank=True, null=True)

    def __str__(self):
        return self.place_title
