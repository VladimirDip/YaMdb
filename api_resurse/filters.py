from django_filters import rest_framework as filter

from .models import Titles


class TitleFilter(filter.FilterSet):
    genre = filter.CharFilter(field_name='genre__slug')
    category = filter.CharFilter(field_name='category__slug')
    year = filter.NumberFilter()
    name = filter.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Titles
        fields = ['genre', 'category', 'year', 'name']
