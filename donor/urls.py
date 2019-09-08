from django.urls import path
from . import views

app_name = 'donor'
urlpatterns = [
	path('', views.index, name='index')
]