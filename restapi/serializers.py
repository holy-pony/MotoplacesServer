from places.models import Place, PlaceType
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    place_type = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='type'
     )

    class Meta:
        model = Place
        fields = ('id', 'place_title', 'place_lat', 'place_lng', 'pub_date', 'place_type')


class PlaceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceType
        fields = ('id', 'type', 'name')
