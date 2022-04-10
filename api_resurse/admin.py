from django.contrib import admin
from api_resurse.models import *


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'year', 'category')
    search_fields = ('category',)
    list_editable = ('category',)


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'text', 'author', 'score', 'pub_date')
    search_fields = ('text', 'score')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


admin.site.register(Titles, TitleAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Genres, GenreAdmin)