from django.urls import path, include
from rest_framework import routers
from .views import CouncilPostViewSet

router = routers.SimpleRouter()
router.register('',CouncilPostViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('', include('router.urls')),
# ]