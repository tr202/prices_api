from csv import DictReader


from django.core.management import BaseCommand
# Import the model 
from api.models import Listing
from pytz import UTC






ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the listings data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from listing-detail.csv"

    def handle(self, *args, **options):
        # Show this when the data already exist in the database
        if Listing.objects.exists():
            print('listings data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        # Show this before loading the data into the database
        print("Loading listings data")

        #Code to load the data into database
        for row in DictReader(open('./listing-details.csv')):
            listing = Listing(session_id=row['session_id'], advertiser_id=row['advertiser_id'], country=row['country'], price=row['price'], event_type_id=row['event_type_id'], gdpr=row['gdpr'], min_cpm=row['min_cpm'], priority=row['priority'], bid_price=row['bid_price'])
            listing.save()
            
