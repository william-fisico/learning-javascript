from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def home2(request):
    return render(request, 'base/home2.html')