from rest_framework.routers import DefaultRouter
from .views import BookviewSet

router = DefaultRouter()
router.register(r'books', BookviewSet, basename='book')
urlpatterns = router.urls
