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



