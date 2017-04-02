from django.shortcuts import render
from django.http import HttpResponse
import time
import re
# Create your views here.

def aNumber():
    sTime = time.strftime("%c")
    sTmp = re.split(':|,| ',sTime)
    iNum = int(sTmp[5])
    return str(iNum * 3)
    
def thePage(request):
    return HttpResponse("Welcome to The Page! Your magicish number this time is: " + time.strftime("%S"))