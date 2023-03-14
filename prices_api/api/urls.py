from rest_framework import routers
from django.urls import include, path

from .views import ListingsViewSet

router = routers.DefaultRouter()
router.register('listings', ListingsViewSet, 'listings')

urlpatterns = [
    path('', include(router.urls)),
]
