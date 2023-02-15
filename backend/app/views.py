from rest_framework import viewsets

from app.models import PostsModel
from app.serializers import PostsSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = PostsModel.objects.all()
    serializer_class = PostsSerializer