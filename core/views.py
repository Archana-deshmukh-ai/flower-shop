from django.shortcuts import render
from django.http import HttpResponse
from flowers.models import Flower  

def home(request):
    flowers = Flower.objects.all()  
    return render(request, 'core/home.html', {'flowers': flowers})


def about_view(request):
    return render(request, 'core/about.html')

def contact_view(request):
    return render(request,'core/contact.html')

def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        return HttpResponse("Thank you for contacting us!")
    return HttpResponse("Invalid request")
