from django.shortcuts import render
import pandas as pd
from django.http import request

# Create your views here.

def trmpage(request):
    
    return render(request,"trm.html")
