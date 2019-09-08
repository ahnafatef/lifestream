from django.http import HttpResponse
from django.shortcuts import render
# from django.shortcuts import redirect

def index(request):
	context = {'req': request.GET}

	return render(request, 'donor/index.html', context)


