from django.urls import path
from .import views


app_name = 'home'

urlpatterns = [
	path('', views.index, name='index'),
	path('dashboard/', views.dashboard, name='dashboard'),
	path('offerapost/', views.offerapost, name='offerapost'),
	path('manageorder/', views.manageorder, name='manageorder'),
	path('jobdetails/', views.jobdetails, name='jobdetails'),
	# path('offerapost/', views.offerapost, name='offerapost'),
    path('offerapost2/', views.offerapost2, name='offerapost2'),
    path('offerapost3/', views.offerapost3, name='offerapost3'),
    path('offerapost4/', views.offerapost4, name='offerapost4'),
    path('orderconfirm/', views.orderconfirm, name='orderconfirm'),
	

] 


