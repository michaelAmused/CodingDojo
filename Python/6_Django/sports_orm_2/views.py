from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count

from . import team_maker

def index(request):
	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }
	#1
	# context = { "teams": Team.objects.filter(league__name="Atlantic Soccer Conference")}
	#2
	# context = { "players": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston")}
	#3
	# context = { "players": Player.objects.filter(curr_team__league__name__contains="Collegiate", curr_team__league__sport="Baseball")}
	#4
	# context = { "players": Player.objects.filter(last_name="Lopez").filter(curr_team__league__name__contains="american conference").filter(curr_team__league__sport__contains="football")}
	#5
	# context = { "players": Player.objects.filter(curr_team__league__sport__contains="football")}
	#6
	# context = { "teams": Team.objects.filter(curr_players__first_name="Sophia")}
	#7
	# context = { "leagues": League.objects.filter(teams__curr_players__first_name="Sophia")}
	#8
	# context = { "players": Player.objects.filter(last_name="Flores").exclude(curr_team__location="Washington").exclude(curr_team__team_name="Rougriders")}
	#9
	# context = { "teams": Team.objects.filter(all_players__last_name="Evans").filter(all_players__first_name="Samuel")}
	#10
	# context = { "players": Player.objects.filter(all_teams__location="Manitoba").filter(all_teams__team_name="Tiger-Cats")}
	#11
	# context = { "players": Player.objects.filter(all_teams__location="Wichita").filter(all_teams__team_name="Vikings").exclude(curr_team__location="Wichita").exclude(curr_team__team_name="Vikings")}
	#12
	# context = { "teams": Team.objects.filter(all_players__last_name="Gray").filter(all_players__first_name="Jacob").exclude(location="Oregon").exclude(team_name="Colts")}
	#13
	# context = { "players": Player.objects.filter(first_name="Joshua").filter(all_teams__league__name__contains="Atlantic Federation of Amateur Baseball Players")}
	#14
	# context = { "teams": Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12)}
	#15
	context = { "players": Player.objects.all().annotate(num_teams=Count('all_teams'))}



	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
