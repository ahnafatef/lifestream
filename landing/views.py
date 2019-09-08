from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
	response = redirect('home/')
	return response


def home(request):
	myobj = {
				'hello': 'hello world',
				'req'  : request.GET
			}
	return render(request, 'landing/home.html', myobj)