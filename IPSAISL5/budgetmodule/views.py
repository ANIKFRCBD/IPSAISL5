from django.shortcuts import render
from django.http import request
from . forms import budget as budgetform
import pandas as pd

budget_account_list_base="DATASOURCE/budget_accounts.csv"
# Create your views here.
def budget(request):
    form_to_collect=budgetform(request.GET)
    if request.method=="GET":
          dataform=budgetform(request.GET)
          if dataform.is_valid():
            formdata=dataform
            #creating new dataframe from the data
            heads=['serial','economiccode','particuars']
            tabledata=[formdata.cleaned_data['serial'], formdata.cleaned_data['economiccode'], formdata.cleaned_data['particulars']]
            df=pd.DataFrame([tabledata],columns=heads)
            #concatanation of data with existing data
            old_data=pd.read_csv(budget_account_list_base)
            print(old_data)
            new_data=pd.concat([old_data,df])
            new_data.to_csv(budget_account_list_base,index=False)
    else:
            print("nothing")
            heads=['serial','economiccode','particuars']
            new_data=pd.DataFrame(columns=heads)
    context={"budget_list":new_data}
    return render(request,"budget.html",context)