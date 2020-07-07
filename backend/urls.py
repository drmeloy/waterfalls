from rest_framework import routers
from .views import WaterfallViewSet

router = routers.DefaultRouter()
router.register('api/waterfalls', WaterfallViewSet, 'waterfalls')

urlpatterns = router.urls