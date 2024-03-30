from django.shortcuts import render
import pandas as pd
from django.http import request,HttpResponse
from pathlib import Path
import numpy as np
from .forms import trmform


# Create your views here.t
source='DATASOURCE/BACS.csv'
source_primary='DATASOURCE/TRM_P.csv'

def trmpage(request):
   dataform=0
   datasource=datareading(request)
   form_to_collect=trmform(request.GET)
   if request.method=="GET":
      dataform=trmform(request.GET)
      if dataform.is_valid():
          formdata=dataform
          tabledata=[formdata.cleaned_data['serial'], formdata.cleaned_data['economiccode'], formdata.cleaned_data['particulars'], formdata.cleaned_data['unit'], formdata.cleaned_data['amount']]
          df=pd.DataFrame([tabledata])
          print(df)
          df.to_csv("DATASOURCE/TRM_P.csv",index=False)
   else:
      print("nothing")
   context={'BACS': datasource,
             'form': form_to_collect}
   return render(request,"trm.html",context)

def datareading(request):
  # Assuming 'source' is the path to your CSV file
  bacs = pd.read_csv(source)
  data_list=bacs["Name"].to_list()
 # Use key 'BACS' for consistency  # Optional, for debugging
  return data_list

