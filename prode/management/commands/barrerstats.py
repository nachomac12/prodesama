from django.core.management.base import BaseCommand
from prode.models import CompetitionStat

class Command(BaseCommand):
    help = 'Update stats for each user'
    def handle(self, *args, **options):
        stats = CompetitionStat.objects.all()
        for c in stats:
            c.get_score()
            c.save()