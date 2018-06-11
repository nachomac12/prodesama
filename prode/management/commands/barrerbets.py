from django.core.management.base import BaseCommand
from prode.models import Bet

class Command(BaseCommand):
    help = 'Update scores for each bet done'
    def handle(self, *args, **options):
        bet_range = Bet.objects.all()
        for bet in bet_range:
            bet.get_result()
            bet.save()