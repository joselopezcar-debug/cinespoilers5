from rest_framework.routers import DefaultRouter
from .views import ShowtimeViewSet

router = DefaultRouter()
router.register(r'showtimes', ShowtimeViewSet)

urlpatterns = router.urls