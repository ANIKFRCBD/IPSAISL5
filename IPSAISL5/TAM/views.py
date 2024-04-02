from django.shortcuts import render,redirect
import pandas as pd
from django.http import request,HttpResponse
from pathlib import Path
import numpy as np

# Create your views here.
source='DATASOURCE/BACS.csv'
transaction_list_for_approval='DATASOURCE/TRM_P.csv'
to_be_approved_list='DATASOURCE/tobeapprovedlist.csv'
TRM='DATASOURCE/TRM.csv'
Final_TRM='DATASOURCE/Final_TRM.csv'

def tampage(request):
    approve=to_be_approved_list
    tam_list=pd.read_csv(approve)
    contex={"tam_list":tam_list.to_html()}
    return render(request,"tam.html",contex)
def tam_list_approver(request):
    to_be_approved_transaction=pd.read_csv(to_be_approved_list)
    old_TRM_final=pd.read_csv(Final_TRM)
    new_final_trm=pd.concat([old_TRM_final,to_be_approved_transaction])
    new_final_trm.to_csv(Final_TRM,index=False)
    to_be_approved_transaction.drop(to_be_approved_transaction.index,inplace=True)
    to_be_approved_transaction.to_csv(to_be_approved_list,index=False)    
    return redirect("tam")