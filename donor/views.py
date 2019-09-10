from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .forms import DonorForm
from .models import Donor

def index(request):
	context = {'req': request.GET}

	return render(request, 'donor/index.html', context)


def add_info(request):
	submitted = False
	if request.method == 'POST':
		form = DonorForm(request.POST)
		if form.is_valid():
			form.save()
			response = redirect('add-info/?submitted=True')
			return response
	else:
		form = DonorForm()
		if 'submitted' in request.GET:
			submitted = True
	context = {'form': form,
				'submitted': submitted
			}
	return render(request, 'donor/add_info_form.html', context)


def search(request):
	data = Donor.objects.all()

	d = [p for p in request.GET.values()]
	if len(d) != 0:
		# starting of query string
		query = 'data.filter('
		for p in request.GET:
			if p == 'blood_group' and request.GET.get(p) != '':

				# use case insensitive regex to search blood_group
				# beginning with param
				query += f"{p}__iregex=r'^{request.GET.get(p)}',"

				# to avoid running the next if block
				continue

			if request.GET.get(p) != '':
				query += f'{p}__icontains="{request.GET.get(p)}",'

		if query[:] == ',':
			query = f'{query[:-1]}'
		query = f'{query})'

		# get the return value of executing the string
		data = eval(query)

	context = {'data': data,
				'request': request.GET
			}
	return render(request, 'donor/search.html', context)
