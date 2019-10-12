from django.http import HttpResponse
from django.http import JsonResponse
from datetime import datetime

def hello(request):
	now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs');
	return HttpResponse('Oh, hi! Current server time is: {now}'.format(now=now));

def hi(request):
	#initialize variables
    response = {}
    numbers = request.GET['numbers']
    #sort a numeric splited list
    response['numbers'] = sorted(list(map(int,numbers.split(','))))
    #response at Json format
    return JsonResponse(response)

def hi2(request, name, age):
	if age <12:
		message = 'Sorry {}, you are not allowed here'.format(name)
	else:
		message = 'Hello {}! Welcome to Seryigram'.format(name)

	return HttpResponse(message)

