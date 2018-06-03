from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Team(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField()
    def __str__(self):
        return self.name

class Match(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    def __str__(self):
        return (self.team1.name + " vs " + self.team2.name)
        
class Bet(models.Model):
    user = models.ForeignKey(User, related_name='bets', blank=True, null=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='bets') 
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'match')

    def __str__(self):
        return (str(self.match))
