from django.db import models


class Listing(models.Model):
    session_id = models.BigIntegerField()
    advertiser_id = models.BigIntegerField()
    country = models.CharField(max_length=5)
    price = models.FloatField()
    event_type_id = models.IntegerField()
    gdpr = models.IntegerField()
    min_cpm = models.FloatField()
    priority = models.FloatField()
    bid_price = models.FloatField()



