from django.shortcuts import render

# Create your views here.
def testing_scripts(request):
    return render(request, 'testing_scripts/testing_scripts.html')

def contador(request):
    context = {'cont':0}
    return render(request, 'testing_scripts/contador.html', context)

def fizzbuzz(request):
    return render(request, 'testing_scripts/fizzbuzz.html')