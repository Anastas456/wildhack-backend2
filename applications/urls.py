from rest_framework import routers
from .api import ApplicationsViewSet
# from django.conf.urls import url
from django.urls.conf import include, path, re_path
from .views import volunteer_application_form


router = routers.DefaultRouter()
router.register('api/applications', ApplicationsViewSet, 'applications')

urlpatterns = [
    path('', include(router.urls))
]
urlpatterns+=[
    re_path(r'^api/applications$', volunteer_application_form)
]