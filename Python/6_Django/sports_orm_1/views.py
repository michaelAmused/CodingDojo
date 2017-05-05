from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }
	#1
	# context = { "leagues": League.objects.filter(name__contains="baseball")}
	#2
	# context = { "leagues": League.objects.filter(name__contains="Women")}
	#3
	# context = { "leagues": League.objects.filter(name__contains="hockey")}
	#4
	# context = { "leagues": League.objects.exclude(name__contains="football")}
	#5
	# context = { "leagues": League.objects.filter(name__contains="conference")}
	#6
	# context = { "leagues": League.objects.filter(name__contains="atlantic")}
	#7
	# context = { "teams": Team.objects.filter(location__contains="Dallas")}
	#8
	# context = { "teams": Team.objects.filter(team_name__contains="Raptors")}
	#9
	# context = { "teams": Team.objects.filter(location__contains="city")}
	#10
	# context = { "teams": Team.objects.all().filter(team_name__startswith='t'}
	#11
	# context = { "teams": Team.objects.all().order_by('location')}
	#12
	# context = { "teams": Team.objects.all().order_by('-team_name') }
	#13
	# context = { "players": Player.objects.filter(last_name = 'Cooper') }
	#14
	# context = { "players": Player.objects.filter(first_name = 'Joshua') }
	#15
	# context = { "players": Player.objects.filter(last_name = 'Cooper').exclude(first_name = 'Joshua') }
	#16
	context = { "players": Player.objects.filter(first_name = 'Alexander')|Player.objects.filter(first_name = 'Wyatt') }











	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
