from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DonorForm
from .models import Donor

def index(request):
	context = {'req': request.GET}

	return render(request, 'donor/index.html', context)


def add_info(request):
	submitted = False;
	if request.method == 'POST':
		form = DonorForm(request.POST)
		if form.is_valid():
			form.save()
			response = redirect('add-info/?submitted=True')
			return response
	else:
		form = DonorForm();
		if 'submitted' in request.GET:
			submitted = True
	context = {'form': form,
				'submitted': submitted
			}
	return render(request, 'donor/add_info_form.html', context)


def search(request):
	data = Donor.objects.all()
	context = {'data': data}
	return render(request, 'donor/search.html', context)
