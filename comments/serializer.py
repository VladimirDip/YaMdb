from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import Reviews, Comments

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    comments = serializers.StringRelatedField(many=True)


    def validate(self, data):
        author = self.context.get('request').user
        title_id = self.context.get('view').kwargs['title_id']
        method = self.context.get('request').method
        if (Reviews.objects.filter(author=author, title=title_id).exists()
                and method == 'POST'):
            raise serializers.ValidationError("You can't write more one review!")
        return data

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date', 'comments']
        read_only_fields = ('title',)
        model = Reviews


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = ['id', 'text', 'author', 'pub_date']
        read_only_fields = ('review',)
        model = Comments
