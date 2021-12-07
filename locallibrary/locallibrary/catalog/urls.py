from django.urls import path
from . import views

urlpatterns = [
	path('', views.index,name='index')
	path('class-name/', vews.ClassName.as_view(), name='Class name list')
    
]