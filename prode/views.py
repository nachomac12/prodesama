from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from prode.forms import RegistrationForm
from .models import Team, Match, Bet
from .forms import BetForm

class MatchView(generic.ListView):
    template_name = 'prode/index.html'
    context_object_name = 'match_list'

    def get_queryset(self):
        """Return all existing match on database"""
        return Match.objects.all()

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

@login_required
class HomeView(generic.ListView):
    template_name = 'prode/home.html'
    def get(self, request):
        return render(request, self.template_name)

class BetView(generic.DetailView):
    template_name = 'prode/apuestas.html'

    #Obtengo todos los elementos de BetForm y todos los partidos de la DB
    def get(self, request):
        matchs = Match.objects.all()
        form = BetForm()
        return render(request, self.template_name, {'form': form, 'matchs': matchs})

    #Guardo los goles de los input en la DB
    def post(self, request, bet_id=None):
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
            return redirect ('home')
        args = {'form': form, 'team1_score': team1_score, 'team2_score': team2_score, 'match': match}
        return render(request, self.template_name, args)

class ScoreView(generic.DetailView):
    template_name = 'prode/puntaje.html'
    def get(self, request):
        return render(request, self.template_name)

class MyDataView(generic.DetailView):
    template_name = 'prode/datos.html'
    def get(self, request):
        return render(request, self.template_name)

class GroupView(generic.DetailView):
    template_name = 'prode/grupos.html'
    def get(self, request):
        return render(request, self.template_name)