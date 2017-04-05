from django.shortcuts import render
from django.http import HttpResponse
import time
# Create your views here.
    
def thePage(request):
    return HttpResponse("Welcome to The Page! Your magicish number this time is: " + time.strftime("%S"))