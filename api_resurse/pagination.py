from rest_framework import pagination
from rest_framework.response import Response


class CustomPagination(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'pervious': self.get_previous_link(),
            'count': self.page.paginator.count,
            'results': data
        })