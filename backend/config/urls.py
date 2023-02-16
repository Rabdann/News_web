from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from app.views import PostsViewSet


router = routers.SimpleRouter()
router.register('posts', PostsViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
