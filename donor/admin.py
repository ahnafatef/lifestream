from django.contrib import admin
from .models import Donor

class DonorAdmin(admin.ModelAdmin):
	list_display = ('name', 'blood_group', 'gender', 'age', 'location', 'phone_number')


admin.site.register(Donor, DonorAdmin)