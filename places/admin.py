from django.contrib import admin

from places.models import Place, PlaceType, Shop

admin.site.register(Place)
admin.site.register(PlaceType)
admin.site.register(Shop)
