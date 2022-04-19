from rest_framework import serializers

from .models import Titles, Categories, Genres


class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ['id']


class GenresSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genres
        exclude = ['id']


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all()
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True
    )

    class Meta:
        model = Titles
        fields = '__all__'


class TitleSerializerGet(serializers.ModelSerializer):
    category = CategoriesSerializers()
    genre = GenresSerializers(many=True)
    # rating = serializers.IntegerField()
    rating = serializers.IntegerField()

    class Meta:
        fields = '__all__'
        model = Titles