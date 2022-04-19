from django.db import models
from django.utils import timezone

from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

from api_resurse.models import Titles


class Reviews(models.Model):
    title = models.ForeignKey(Titles, on_delete=models.CASCADE, related_name='reviews')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'


class Comments(models.Model):
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super().save(*args, **kwargs)

