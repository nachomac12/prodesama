from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from prode.forms import RegistrationForm
from .models import Team, Match, Bet, Competition, CompetitionStat
from .forms import BetForm
from django.utils import timezone
import datetime


class IndexView(generic.ListView):
    template_name = 'prode/index.html'
    context_object_name = 'match_list'

    def get_queryset(self):
        """Return all existing match on database."""
        return Match.objects.filter(competition__available=True).filter(end__gte=timezone.now()).order_by('start')[:10]

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse('prode:home'))
    else:
        form = RegistrationForm()
    return render(request, 'prode/signup.html', {'form': form})


class HomeView(generic.ListView):
    template_name = 'prode/home.html'
    def get(self, request):
        return render(request, self.template_name)


class BetView(generic.DetailView):
    template_name = 'prode/apuestas.html'

    #Obtengo todos los elementos de BetForm y todos los partidos de la DB
    def get(self, request):
        m = Match.objects.all().order_by('start')
        matchs = []
        for i in m:
            if i.is_unavailable() == False:
                matchs.append(i)
        competitions = Competition.objects.filter(available=True)
        form = BetForm()
        bets = Bet.objects.all()
        args = {'form': form, 'matchs': matchs, 'bets': bets, 'competitions': competitions}
        return render(request, self.template_name, args)

    #Guardo los goles de los input en la DB
    def post(self, request):
        bet_id = request.POST.get("bet_id")
        if bet_id:
            bet = Bet.objects.get(pk=bet_id)
            form = BetForm(request.POST, instance=bet)
        else:
            form = BetForm(request.POST)
        if form.is_valid():
            bet = form.save(commit=False)
            bet.user = request.user
            bet.save()
            team1_score = form.cleaned_data.get('team1_score')
            team2_score = form.cleaned_data.get('team2_score')
            match = form.cleaned_data.get('match')
            form = BetForm()
            return redirect ('prode:home')
        args = {'form': form, 'team1_score': team1_score, 'team2_score': team2_score, 'match': match}
        return render(request, self.template_name, args)


class ScoreView(generic.DetailView):
    template_name = 'prode/puntaje.html'
    def get(self, request):
        comp_stats = CompetitionStat.objects.all()
        return render(request, self.template_name, {'comp_stats':comp_stats})


class MyDataView(generic.DetailView):
    template_name = 'prode/datos.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        user_id = request.POST.get("user_id")
        if user_id:
            user = User.objects.get(pk=user_id)
            user.first_name = request.POST["first_name"]
            user.last_name = request.POST["last_name"]
            user.username = request.POST["username"]
            user.save()
            return redirect('prode:home')
        return render(request, self.template_name)

class GroupView(generic.DetailView):
    template_name = 'prode/grupos.html'
    def get(self, request):
        return render(request, self.template_name)