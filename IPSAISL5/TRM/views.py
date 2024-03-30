from django.shortcuts import render
import pandas as pd
from django.http import request
from pathlib import Path
import numpy as np
from .forms import trmform


# Create your views here.t
source='DATASOURCE/BACS.csv'

def trmpage(request):
    datasource=datareading(request)
    form=formprocessing(request)
    context={'BACS': datasource.tolist(),"form":form}
    return render(request,"trm.html",context)

def formprocessing(request):
   dataform=0
   if request.method=="GET":
      dataform=trmform(request.GET)
      if dataform.is_valid():
         dataform=dataform
         print(dataform)
   else:
      print("nothing")
   return dataform

def datareading(request):
  # Assuming 'source' is the path to your CSV file
  bacs = pd.read_csv(source)
  html_table = bacs['Name']
 # Use key 'BACS' for consistency  # Optional, for debugging
  return html_table

