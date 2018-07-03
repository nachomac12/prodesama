from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import timedelta


class Team(models.Model):
    name = models.CharField(max_length=50)
    flag = models.ImageField(upload_to='prode/images/flags/')
    def __str__(self):
        return self.name


class Competition(models.Model):
    name = models.CharField(max_length=100)
    available = models.BooleanField(default=False)

    def __str__(self):
        return (str(self.name))


class Match(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='+')
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    def end_match(self):
        now = timezone.now() 
        return self.end <= now

    def get_endscore(self):
        winner = None
        if (self.end_match() == True):
            if (self.team1_score > self.team2_score):
                winner = self.team1
            elif (self.team1_score < self.team1_score):
                winner = self.team2
            elif (self.team1_score == self.team2_score):
                winner = "tie"
        return winner

    def is_unavailable(self):
        now = timezone.now()
        start = self.start - timedelta(hours=1)
        return now >= start

    def __str__(self):
        return (self.team1.name + " vs " + self.team2.name)
        
        
class Bet(models.Model):
    user = models.ForeignKey(User, related_name='bets', blank=True, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name='bets') 
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    result = models.PositiveIntegerField(default=0, null=True)
    calculated = models.BooleanField(default=False)

    def get_result(self):
            if (self.match.get_endscore() == self.match.team1) and (self.team1_score > self.team2_score):
                self.result = 1
            elif (self.match.get_endscore() == self.match.team2) and (self.team2_score > self.team1_score):
                self.result = 1
            elif (self.match.end_match()==True) and (self.match.team1_score == self.team1_score) and (self.match.team2_score == self.team2_score):
                self.result = 3
            elif (self.match.get_endscore() == "tie") and (self.team1_score == self.team2_score):
                self.result = 1
            else: 
                self.result = 0
            return self.result
    #class Meta:
    #    unique_together = ('user', 'match')

    def __str__(self):
        return (str(self.match))


class CompetitionStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comps')
    score = models.PositiveIntegerField(default=0)
    ranking = models.PositiveIntegerField(null=True)
    comp = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True, related_name='comps')

    def get_score(self):
        lista = [self.user.bets.all()] 
        for elem in lista:
            for i in elem:
                if (self.comp == i.match.competition):
                    if i.calculated == False and i.match.end_match() == True:
                        self.score += i.result
                        i.calculated = True
                        i.save()
        return self.score

    def get_ranking(self):
        comp_stats = CompetitionStat.objects.filter(comp=self.comp).order_by('-score')
        lista = [cs for cs in comp_stats]
        for elem in lista:
            if (elem.user == self.user):
                self.ranking = lista.index(elem) + 1
        return self.ranking

    def __str__(self):
        return(str(self.user) + " - " + str(self.comp))

    class Meta:
        unique_together = ('user', 'comp')