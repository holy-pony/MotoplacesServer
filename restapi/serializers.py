from places.models import Place, PlaceType
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Place
        fields = ('id', 'place_title', 'place_lat', 'place_lng', 'pub_date', 'place_type')


class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = ('id', 'place_type', 'place_type_name')
