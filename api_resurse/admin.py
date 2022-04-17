from django.contrib import admin
from api_resurse.models import *


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'year', 'category')
    search_fields = ('category',)
    list_editable = ('category',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')


admin.site.register(Titles, TitleAdmin)
admin.site.register(Genres, GenreAdmin)