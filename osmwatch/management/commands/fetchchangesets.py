from django.core.management.base import BaseCommand, CommandError
from cities.models import City
from osmwatch.models import City

class Command(BaseCommand):
    help = 'fetches changesets made to OSM on a daily basis for specific bounding boxes'
    def handle(self, *args, **options):
        self.stdout.write("This is a test for the management command")
