from django.shortcuts import render
import pandas as pd
from django.http import request
from pathlib import Path
import numpy as np


# Create your views here.t
source='DATASOURCE/BACS.csv'

def trmpage(request):
    datasource=datareading(request)
    context={'BACS': datasource.tolist()}
    print(context)
    return render(request,"trm.html",context)

def datareading(request):
  # Assuming 'source' is the path to your CSV file
  print(request.method)
  bacs = pd.read_csv(source)
  html_table = bacs['Name']
 # Use key 'BACS' for consistency  # Optional, for debugging
  return html_table

