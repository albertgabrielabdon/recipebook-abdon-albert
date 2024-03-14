from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Task

def index(request):
    return HttpResponse('Hello World')

def task_list(request):
    sf
    
def task_detail(request, pk):
    s

class TaskListView(ListView):
    s
    
class TaskDetailView(LoginRequiredMixin, DetailView):
    s
    
 
# Create your views here.
