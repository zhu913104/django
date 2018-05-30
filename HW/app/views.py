from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import redirect 
from datetime import datetime
from app.models import Commodity
from django.http import HttpResponse
from dwebsocket import require_websocket
from dwebsocket.decorators import accept_websocket,require_websocket
import serial
from collections import defaultdict   
allconn = defaultdict(list) 
# Create your views here.

def hello(request):
	return render(request,'hello.html',{'current_time':str(datetime.now())})

def commodity(request):
	commodity=Commodity.objects.all()
	commodity_id = Commodity._meta.get_field('commodity_id').column
	commodity_name = Commodity._meta.get_field('commodity_name').column
	commodity_num = Commodity._meta.get_field('commodity_num').column
	commodity_date = Commodity._meta.get_field('commodity_date').column
	commodity_dis = Commodity._meta.get_field('commodity_dis').column
	commodity_img = Commodity._meta.get_field('commodity_img').column
	commodity_price = Commodity._meta.get_field('commodity_price').column
	return render_to_response('commodity.html',locals())

def insert(request):
	return render(request,'insert.html')

def do_insert(request):
	try:
		commodity_name = request.POST['commodity_name']
		commodity_num = request.POST['commodity_num']
		commodity_date = request.POST['commodity_date']
		commodity_dis = request.POST['commodity_dis']
		commodity_img =request.POST['commodity_img']
		commodity_price = request.POST['commodity_price']
		Commodity.objects.create(commodity_name=commodity_name,commodity_num=commodity_num,commodity_date=commodity_date,commodity_dis=commodity_dis,commodity_img=commodity_img,commodity_price=commodity_price)
		return HttpResponse(200)
	except Exception as e:
		return HttpResponse(e)

def detail(request, commodity_id):
	detail = Commodity.objects.get(commodity_id=commodity_id)
	return render(request,'detail.html', {'detail': detail})

def do_update(request):
	try:
		commodity_id = request.POST['commodity_id']
		commodity_name = request.POST['commodity_name']
		commodity_num = request.POST['commodity_num']
		commodity_date = request.POST['commodity_date']
		commodity_dis = request.POST['commodity_dis']
		commodity_img = request.POST['commodity_img']
		commodity_price = request.POST['commodity_price']
		do_update = Commodity.objects.filter(commodity_id=commodity_id)
		do_update.update(commodity_name=commodity_name)
		do_update.update(commodity_name=commodity_num)
		do_update.update(commodity_date=commodity_date)
		do_update.update(commodity_dis=commodity_dis)
		do_update.update(commodity_img=commodity_img)
		do_update.update(commodity_price=commodity_price)
		return HttpResponse(200)
	except Exception as e:
		return HttpResponse(e)


	return redirect('/commodity/')

def update(request,commodity_id):
	update = Commodity.objects.get(commodity_id=commodity_id)
	return render(request,'update.html',{'update':update})

def do_delete(request):
	try:
		commodity_id = request.POST['commodity_id']
		do_delete = Commodity.objects.filter(commodity_id=commodity_id)
		do_delete.delete()
		return HttpResponse(200)
	except Exception as e:
		return	HttpResponse(commodity_id)

def delete(request,commodity_id):
	delete = Commodity.objects.get(commodity_id=commodity_id)
	return render(request,'delete.html',{'delete':delete})

def index(request):
	return render(request,'index.html')

def index2(request):
	return render(request,'index2.html')

@require_websocket
def echo_once(request):
    message = request.websocket.wait()
    request.websocket.send(message)

def modify_message(message):
    return message.lower()



@accept_websocket
def echo(request,userid):
	# ser=serial.Serial("COM3",9600,timeout=100)
	allresult = {} 
	allresult['userid'] = userid
	global allconn 
	if not request.is_websocket():#判断是不是websocket连接
		try:#如果是普通的http方法
			message = request.GET['message']
			return HttpResponse(message)
		except:
			return render(request,'index2.html',allresult)
	else:
		allconn[str(userid)] = request.websocket
		for message in request.websocket:
			try:
				# serin = message+str("\n").encode()
				# ser.write(serin)
				# message=str("Server return: ").encode()+message
				request.websocket.send (message)#发送消息到客户端
				for i in allconn:  
					if i != str(userid):  
						allconn[i].send(message)
			except Exception as e:
				pass

	ser.close()

	

