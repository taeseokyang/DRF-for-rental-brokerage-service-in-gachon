from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet

router = routers.SimpleRouter()
router.register('posts',PostViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('', include('router.urls')),
# ]