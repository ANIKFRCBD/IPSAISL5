from django.shortcuts import render,redirect
import pandas as pd
from django.http import request,HttpResponse
from pathlib import Path
import numpy as np
from .forms import trmform


# Create your views here.t
source='DATASOURCE/BACS.csv'
transaction_list_for_approval='DATASOURCE/TRM_P.csv'
to_be_approved_list='DATASOURCE/tobeapprovedlist.csv'

def trmpage(request):
   dataform=0
   datasource=datareading(request)
   form_to_collect=trmform(request.GET)
   if request.method=="GET":
      dataform=trmform(request.GET)
      if dataform.is_valid():
          formdata=dataform
          #creating new dataframe from the data
          heads=['serial','economiccode','particuars','unit','amount']
          tabledata=[formdata.cleaned_data['serial'], formdata.cleaned_data['economiccode'], formdata.cleaned_data['particulars'], formdata.cleaned_data['unit'], formdata.cleaned_data['amount']]
          df=pd.DataFrame([tabledata],columns=heads)
          #concatanation of data with existing data
          old_data=pd.read_csv(transaction_list_for_approval)
          new_data=pd.concat([old_data,df])
          new_data.to_csv(transaction_list_for_approval,index=False)
   else:
      print("nothing")
   trm_list_for_approval=trmlister(transaction_list_for_approval)
   print(trm_list_for_approval)
   context={'BACS': datasource,
             'form': form_to_collect,
             'trm_list':trm_list_for_approval.to_html}
   return render(request,"trm.html",context)

def datareading(request):
  # Assuming 'source' is the path to your CSV file
  bacs = pd.read_csv(source)
  data_list=bacs["Name"].to_list()
 # Use key 'BACS' for consistency  # Optional, for debugging
  return data_list

def trmlister(transaction_list_for_approval):
   for_approval_list=pd.read_csv(transaction_list_for_approval)
   return for_approval_list

def trm_list_approver(request):
   to_be_approved_list=pd.read_csv(transaction_list_for_approval)
   to_be_approved_list.to_csv('DATASOURCE/tobeapprovedlist.csv',index=False)
   to_be_approved_list.drop(to_be_approved_list.index,inplace=True)
   to_be_approved_list.to_csv(transaction_list_for_approval,index=False)
   return redirect("homepage")
