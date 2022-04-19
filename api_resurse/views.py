import mixins as mixins
from django.db.models import Avg
from rest_framework import status, filters, viewsets, mixins
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Titles, Genres, Categories
from .serializers import (TitleSerializerGet,
                          GenresSerializers,
                          CategoriesSerializers,
                          TitleSerializer)
from .filters import TitleFilter
from .permissions import IsAdminOnReadOnly

class MixinView(mixins.CreateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                viewsets.GenericViewSet):
    pass


class GenreViewSet(MixinView):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    lookup_field = 'slug'
    http_method_names = ['get', 'post', 'delete']
    permission_classes = [IsAdminOnReadOnly,]


class CategoryViewSet(MixinView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']
    http_method_names = ['get', 'post', 'delete']
    lookup_field = 'slug'
    permission_classes = [IsAdminOnReadOnly]


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.annotate(rating = Avg('reviews__score'))
    filter_backends = [DjangoFilterBackend]
    filterset_class = TitleFilter
    permission_classes = [IsAdminOnReadOnly,]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TitleSerializerGet
        else:
            return TitleSerializer