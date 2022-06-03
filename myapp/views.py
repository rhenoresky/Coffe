from django.shortcuts import render
from .models import Logo

# Create your views here.

def index(request):
    logo = Logo.objects.get(id=1)
    return render(request,'index.html',{'logo':logo})