from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField()
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Match(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    print(str(team1))

class Bet(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='+')
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)