from django.contrib import admin

from places.models import Place, PlaceType, Shop, Location

admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(Shop)
admin.site.register(Location)
