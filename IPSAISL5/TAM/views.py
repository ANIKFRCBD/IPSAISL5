from django.shortcuts import render,redirect
import pandas as pd
from django.http import request,HttpResponse
from pathlib import Path
import numpy as np
from .forms import trmform

# Create your views here.
source='DATASOURCE/BACS.csv'
transaction_list_for_approval='DATASOURCE/TRM_P.csv'
to_be_approved_list='DATASOURCE/tobeapprovedlist.csv'
TRM='DATASOURCE/TRM.csv'

def approver(request):
    to_be_approved_transaction=pd.read_csv(to_be_approved_list)
    to_be_approved_transaction.to_csv(TRM,index=False)
    return HttpResponse("Done")