from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from prode.forms import RegistrationForm
from .models import Team, Match, Bet

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
    context_object_name = 'bet_list'
    
    def get_queryset(self):
        return Bet.objects.all()

    #Armar función POST que guarde en la DB los input de goles