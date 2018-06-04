from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect
from datetime import datetime
from django.http import HttpResponse
from dwebsocket import require_websocket
from dwebsocket.decorators import accept_websocket,require_websocket
import serial
from collections import defaultdict
from app.RL import *
# Create your views here.
def hello(request):
	return render(request,'hello.html',{'current_time':str(datetime.now())})


def game(request):
	return render(request,'tictactoe.html')
def result(request):
	observation = request.POST['board']
	legal = request.POST['legal']

	print(legal)
	ai = QLearningTable(actions=['1','2','3','4','5','6','7','8','0'], file="XX.csv", e_greedy=1)
	action  = str(ai.choose_action(str(observation)))
	while  not(observation[1+int(action)*2-1] == " ") and legal:
		action = str(ai.choose_action(str(observation),False))
	print(action)
	if legal:
		return HttpResponse(action)
	else:
		return HttpResponse(200)
