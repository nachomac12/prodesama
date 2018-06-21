from django.contrib import admin
from .models import Team, Match, Bet, Competition, CompetitionStat

admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Bet)
admin.site.register(Competition)
admin.site.register(CompetitionStat)