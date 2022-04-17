from django.db import models
from django.core.validators import MaxValueValidator

from .utils import current_year


class Titles(models.Model):
    name = models.CharField(max_length=200,
                            blank=True,
                            verbose_name='titles')
    year = models.IntegerField(validators=[MaxValueValidator(current_year())],
                               null=True,
                               db_index=True)
    category = models.ForeignKey('Categories',
                                 on_delete=models.SET_NULL,
                                 related_name='titles',
                                 blank=True,
                                 null=True)
    genre = models.ManyToManyField('Genres', blank=True)
    description = models.TextField(blank=True,
                                   null=True)

    class Meta:
        verbose_name = 'Titles'
        verbose_name_plural = 'Title'

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='categories')
    slug = models.SlugField(max_length=50,
                            blank=True,
                            null=True,
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'


class Genres(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True,
                            verbose_name='genres')
    slug = models.SlugField(max_length=50,
                            blank=True,
                            null=True,
                            unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Genres'
        verbose_name = 'Genre'


# class Reviews(models.Model):
#     title = models.ForeignKey('Titles', on_delete=models.CASCADE, related_name='reviews')
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
#     score = models.IntegerField()
#     pub_date = models.DateTimeField('date published', auto_now_add=True)
#
#     class Meta:
#         verbose_name = 'Отзыв'
#         verbose_name_plural = 'Отзывы'
#
#
# class Comments(models.Model):
#     review = models.ForeignKey('Reviews', on_delete=models.CASCADE, related_name='comments')
#     text = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     pub_date = models.DateTimeField('date published', auto_now_add=True)


# class Genre_title(models.Model):
#     title = models.ForeignKey('Titles', on_delete=models.SET_NULL,
#                               related_name='title',
#                               blank=True,
#                               null=True)
#     genre = models.ForeignKey('Genres', on_delete=models.SET_NULL,
#                               related_name='genre',
#                               blank=True,
#                               null=True)
