from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets

from api_resurse.models import Titles

from .models import Reviews
from .permission import IsAuthorOrAdmin
from .serializer import CommentSerializer, ReviewSerializer


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrAdmin
    ]

    def get_title(self):
        title = get_object_or_404(Titles, id=self.kwargs['title_id'])
        return title

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(author=self.request.user, title=title)


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsAuthorOrAdmin
    ]

    def get_review(self):
        review = get_object_or_404(
            Reviews,
            id=self.kwargs['review_id'],
            title__id=self.kwargs['title_id']
        )
        return review

    def get_queryset(self):
        review = self.get_review()
        return review.comments.all()

    def perform_create(self, serializer):
        review = self.get_review()
        serializer.save(author=self.request.user, review=review)
