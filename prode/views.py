from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import generic    #TemplateView
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from prode.forms import RegistrationForm
from .models import Team, Match, Bet, Competition, CompetitionStat
from .forms import BetForm
from django.utils import timezone
import datetime
from datetime import timedelta
import json


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
def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'Ese nombre de usuario ya está registrado. Ingrese otro.'
    return JsonResponse(data)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, _('Tu contraseña ha sido modificada'))
            return redirect('prode:datos')
        else:
            messages.error(request, _('Las contraseñas deben coincidir.'))
            return redirect('prode:datos')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'prode/change_password.html', {'form': form})


class IndexView(generic.ListView):
    template_name = 'prode/index.html'
    
    def get(self, request):
        matches = Match.objects.filter(competition__available=True).filter(end__gte=timezone.now()).order_by('start')[:4]
        comp_stats = CompetitionStat.objects.filter(ranking__lte=5).order_by('ranking')
        competition = Competition.objects.filter(available=True)
        args = {'matches': matches, 'competition':competition ,'comp_stats': comp_stats}
        return render(request, self.template_name, args)


class HomeView(generic.ListView):
    template_name = 'prode/home.html'
    def get(self, request):
        return render(request, self.template_name)


class BetView(generic.DetailView):
    template_name = 'prode/apuestas.html'

    def get(self, request):
        form = BetForm()
        m = Match.objects.filter(competition__available=True).order_by('start')
        matchs = []
        for i in m:
            if i.is_unavailable() == False:
                matchs.append(i)
        bets = Bet.objects.all()
        competitions = Competition.objects.filter(available=True)
        args = {'form': form, 'matchs': matchs[:10], 'bets': bets,
                'competitions': competitions}
        return render(request, self.template_name, args)

    def post(self, request):
        bet_id = request.POST.get("bet_id")
        if bet_id and request.user.bets.get(id=bet_id):
            bet = Bet.objects.get(id=bet_id)
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
            if request.user.comps.exists()==False:
                cs = CompetitionStat()
                cs.user = request.user
                cs.comp = Competition.objects.get(name="Copa Libertadores")
                cs.save()
            messages.info(request, "Apuesta realizada!")
            return redirect ('prode:apuestas')
        args = {'form': form, 'team1_score': team1_score, 'team2_score': team2_score, 'match': match}
        return render(request, self.template_name, args)


class ScoreView(generic.DetailView):
    template_name = 'prode/puntaje.html'
    def get(self, request):
        comps = Competition.objects.filter(available=True)
        comp_stats = CompetitionStat.objects.all()
        bets = Bet.objects.all()
        return render(request, self.template_name, {'comps':comps,'comp_stats':comp_stats, 'bets':bets})


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
            messages.success(request, 'Tus datos se han modificado', extra_tags='alert')
            return redirect('prode:datos')
        return render(request, self.template_name)

# class GroupView(generic.DetailView):
#     template_name = 'prode/grupos.html'
#     def get(self, request):
#         return render(request, self.template_name)
