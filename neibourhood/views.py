from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(homepage)

def add_hood(request):
    return render(add_hood)

def add_biz(request):
    return render(add_biz)

def add_post(request):
    return render(add_post)

def search_results(request):
    return render(search_results)    

def user(request):
    return render(user)       
