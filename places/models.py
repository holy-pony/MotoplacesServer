from django.db import models


class PlaceType(models.Model):
    place_type = models.CharField(max_length=16)
    place_type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.place_type_name


class Place(models.Model):
    place_title = models.CharField(max_length=200) #blank=True, null=True
    place_lat = models.FloatField()
    place_lng = models.FloatField()
    pub_date = models.DateTimeField('date published')
    place_type = models.ForeignKey(PlaceType)

    def __str__(self):
        return self.place_title
