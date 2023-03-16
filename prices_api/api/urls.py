from django.urls import include, path
from rest_framework import routers

from .views import ListingsViewSet

router = routers.DefaultRouter()
router.register('listings', ListingsViewSet, 'listings')

urlpatterns = [
    path('', include(router.urls)),
]
