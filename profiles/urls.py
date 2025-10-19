# profiles/urls.py
from rest_framework.routers import DefaultRouter
from .views import AthleteProfileViewSet, CoachViewSet, AgentViewSet

router = DefaultRouter()
router.register(r"athletes", AthleteProfileViewSet, basename="athlete")
router.register(r"coaches", CoachViewSet, basename="coach")
router.register(r"agents", AgentViewSet, basename="agent")

urlpatterns = router.urls
