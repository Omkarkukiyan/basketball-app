from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from team.models import Players 
from team.forms import PlayerForm 


@login_required
def team(request):
    players = Players.objects.all()
    context = {
        'players' : players
    } 
    return render(request, 'team/team.html', context)
