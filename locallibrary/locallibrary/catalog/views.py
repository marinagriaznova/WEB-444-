from django.shortcuts import render
from django.views import generic
from .models import BookModel, BookInstanceModel, AuthorModel

def index(request):
	num_books =
	num_instances =
	num_instances_available

class ClassName(generic.ListView):
	model = ClassNameModel
	context_objects_name = 'books_list'
	queryset = ClassNameModel.objects.all()
	template_name = 'class_name_list.html'