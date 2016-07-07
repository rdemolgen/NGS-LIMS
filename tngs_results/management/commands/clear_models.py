from django.core.management.base import BaseCommand
from tngs_results.models import Sample_list

class Command(BaseCommand):
    def handle(self, *args, **options):
        Sample_list.objects.all().delete()


