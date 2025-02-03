from django.shortcuts import render
a = {
    'title': 'Local'
}
# Create your views here.

def local(request):
    return render(request, 'local/index.html', a)