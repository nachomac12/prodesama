from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField()
    def __str__(self):
        return self.name

# class Match(models.Model):
#     start = models.DateTimeField()
#     end = models.DateTimeField()
#     team1 = models.ForeignKey(Team, on_delete=models.CASCADE)
    # team2 = models.ForeignKey(Team, on_delete=models.CASCADE)
    # team1_score = models.PositiveIntegerField()
    # team2_score = models.PositiveIntegerField()