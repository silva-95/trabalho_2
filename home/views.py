from django.shortcuts import render
a = {
    'title': 'Home'}
# Create your views here.

def home(request):
    return render(request, 'home/index.html', a)