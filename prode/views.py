from django.shortcuts import render
from django.views import generic
from .models import Team, Match

class IndexView(generic.ListView):
    template_name = 'prode/index.html'
    context_object_name = 'match_list'

    def get_queryset(self):
        """Return all existing teams on database"""
        return Match.objects.all()