from django.shortcuts import render
from django.views import generic
from .models import Team

class IndexView(generic.ListView):
    template_name = 'prode/index.html'
    context_object_name = 'team_list'

    def get_queryset(self):
        """Return all existing teams on database"""
        return Team.objects.all()