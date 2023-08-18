from django.urls import path, include
from rest_framework import routers
from .views import CommentViewSet, BorrowDone

router = routers.SimpleRouter()
router.register('',CommentViewSet)
# router.register('done',BorrowDone,basename='done')
# urlpatterns = router.urls
urlpatterns = [
    path('done/<int:writer>/<int:commentid>', BorrowDone.as_view()),
    path('', include(router.urls))

]#url 어케 해야해????