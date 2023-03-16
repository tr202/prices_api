from rest_framework import viewsets

from .models import Listing
from .serializers import ListingSerializer


class ListingsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

    def get_queryset(self):
        r = self.request
        min_price = r.GET.get('min_price')
        max_price = r.GET.get('max_price')
        min_min_cpm = r.GET.get('min_min_cpm')
        max_min_cpm = r.GET.get('max_min_cpm')
        return Listing.objects.filter(price__range=(min_price, max_price),
                                      min_cpm__range=(min_min_cpm, max_min_cpm))
