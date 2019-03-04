from webapp.models import Movie, Category, Hall, Seat, Show
from rest_framework import serializers


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api_v1:movie-detail')

    class Meta:
        model = Movie
        fields = ('url', 'id', 'name', 'description', 'poster', 'release_date', 'finish_date')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title', 'description')


class HallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('id', 'title')


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ('id', 'hall', 'row', 'seat')


class ShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Show
        fields = ('id', 'movie', 'hall', 'start_time', 'finish_time', 'price')