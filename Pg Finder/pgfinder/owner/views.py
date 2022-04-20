from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.







def ContactUs(request):
    return render(request, 'owner/ContactUs.html')

   
def AboutUs(request):   
    return render(request, 'owner/AboutUs.html')

def index(request):   
    return render(request, 'owner/index.html')

