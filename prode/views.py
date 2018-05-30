from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from prode.forms import RegistrationForm
from .models import Team, Match, Bet
from .forms import BetForm

class IndexView(generic.ListView):
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
            return HttpResponseRedirect(reverse('prode:index'))
            #return redirect('home')    
    else:
        form = RegistrationForm()
        return render(request, 'prode/signup.html', {'form': form})

class BetView(generic.ListView):  
    template_name = 'prode/home.html'
  
    def get(self, request):
        form = BetForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):  
        form = BetForm(request.POST)
        if form.is_valid():
            form.save() 
            team1_score = form.cleaned_data.get('team1_score')
            team2_score = form.cleaned_data.get('team2_score')
            form = BetForm()
        args = {'form': form, 'team1_score': team1_score, 'team2_score': team2_score}
        return render(request, self.template_name, args)

