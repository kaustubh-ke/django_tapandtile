from django.urls import path

from . import views

app_name = 'firstapp'

urlpatterns = [
	path('', views.index, name= 'index'),
	path('index', views.index),
	path('about',views.about),


]