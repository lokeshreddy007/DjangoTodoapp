from django.shortcuts import render
from .models import List

def home(request):
    data = List.objects.all
    return render(request,'home.html',{'data':data})



def about(request):
    data={'fristname':'lokesh','second_name':'reddy'}
    return render(request,'about.html',data)