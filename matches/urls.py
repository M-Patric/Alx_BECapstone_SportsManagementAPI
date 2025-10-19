# matches/urls.py
from rest_framework.routers import DefaultRouter
from .views import TalentAgentLinkViewSet

router = DefaultRouter()
router.register(r"matches", TalentAgentLinkViewSet, basename="match")
urlpatterns = router.urls
