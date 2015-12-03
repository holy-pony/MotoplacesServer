from django.contrib import admin

from places.models import Place, PlaceType, Shop


class PlacesAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "place_type":
            qs = kwargs.get('queryset', db_field.rel.to.objects)
            kwargs['queryset'] = qs.select_related('place_type')
        return super(PlacesAdmin, self).formfield_for_manytomany(db_field, request, **kwargs)

admin.site.register(Place, PlacesAdmin)
admin.site.register(PlaceType)
admin.site.register(Shop)

# Register your models here.
