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

	if request.method == 'GET':
		blood_group = request.GET.get('blood_group')
		print(blood_group)
		age = request.GET.get('age')
		gender = request.GET.get('gender')
		location = request.GET.get('location')

		if blood_group != '' and blood_group is not None:
			data = data.filter(blood_group__icontains=blood_group)

		elif age != '' and age is not None:
			data = data.filter(age__icontains=age)

		elif gender != '' and gender is not None:
			data = data.filter(gender__icontains=gender)

		elif location != '' and location is not None:
			data = data.filter(location__icontains=location)

	context = {'data': data}
	return render(request, 'donor/search.html', context)
