from rest_framework import serializers as s

from .models import Listing


class ListingSerializer(s.ModelSerializer):
    class Meta:
        model = Listing
        fields = ('advertiser_id', 'country', 'price', 'event_type_id', 'gdpr', 'min_cpm', 'priority', 'bid_price' )
    
