# training/urls.py
from rest_framework.routers import DefaultRouter
from .views import TrainingSessionViewSet, PerformanceRecordViewSet

router = DefaultRouter()
router.register(r"training-sessions", TrainingSessionViewSet, basename="training-session")
router.register(r"performance-records", PerformanceRecordViewSet, basename="performance-record")
urlpatterns = router.urls
