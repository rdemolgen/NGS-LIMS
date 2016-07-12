from django.core.management.base import BaseCommand
from tngs_results.models import Sample_list
from ClinSci.models import Batch

class Command(BaseCommand):
    def handle(self, *args, **options):
        Sample_list.objects.all().delete()
        Batch.objects.all().delete()


