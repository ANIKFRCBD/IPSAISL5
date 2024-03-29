from django.shortcuts import render
import pandas as pd
from django.http import request
from pathlib import Path


# Create your views here.t
source='DATASOURCE/BACS.csv'

def trmpage(request):
    datareading(request)
    return render(request,"trm.html")

def datareading(request):
    bacs=pd.read_csv(source)
    html_table=bacs.to_html(escape=False)
    context={"BACS":html_table}
    print(context)
    return render (request, 'trm.html', context )

