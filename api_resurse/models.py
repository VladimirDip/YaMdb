from django.db import models


class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=200)
    email = models.EmailField()
    role = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    category = models.ForeignKey('Categories', on_delete=models.SET_NULL,
                                 related_name='titles',
                                 blank=True,
                                 null=True)

    class Meta:
        verbose_name = 'Название'
        verbose_name_plural = 'Названия'


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    title = models.ForeignKey('Titles', on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Comments(models.Model):
    review = models.ForeignKey('Reviews', on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('date published', auto_now_add=True)


class Genre_title(models.Model):
    title = models.ForeignKey('Titles', on_delete=models.SET_NULL,
                              related_name='title',
                              blank=True,
                              null=True)
    genre = models.ForeignKey('Genres', on_delete=models.SET_NULL,
                              related_name='genre',
                              blank=True,
                              null=True)
