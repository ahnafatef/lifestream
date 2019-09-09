from django.urls import path
from . import views

app_name = 'donor'
urlpatterns = [
	path('', views.add_info, name='index'),
	path('add-info/', views.add_info, name='add-info'),
	path('search/', views.search, name='search'),
]