from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions

from tweets.models import Tweet

from .pagination import StandardResultsPagination
from .serializers import TweetModelSerializer

class TweetCreateAPIView(generics.CreateAPIView):
    serializer_class = TweetModelSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TweetListAPIView(generics.ListAPIView):
    serializer_class = TweetModelSerializer
    pagination_class = StandardResultsPagination

    def get_queryset(self, *args, **kwargs):
        im_following = self.request.user.profile.get_following() # none
        qs1 = Tweet.objects.filter(user__in=im_following)
        qs2 = Tweet.objects.filter(user=self.request.user)
        qs = (qs1 | qs2).distinct().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query)
                )
        return qs
