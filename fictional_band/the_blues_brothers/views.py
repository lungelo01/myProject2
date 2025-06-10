from django.shortcuts import render

"""home view

"""
# Create your views here.
def home(request):
    return render(request, 'home.html')
