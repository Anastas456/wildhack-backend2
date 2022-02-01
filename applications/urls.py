from rest_framework import routers
from .api import ApplicationsViewSet


router = routers.DefaultRouter()
router.register('api/applications', ApplicationsViewSet, 'applications')

urlpatterns = router.urls