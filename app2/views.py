from django.shortcuts import render
import app1
# Create your views here.

def home(request):
    return render(request, 'home.html')