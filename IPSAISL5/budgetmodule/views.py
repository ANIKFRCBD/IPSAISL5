from django.shortcuts import render
from django.http import request
from . forms import budget as budgetform
import pandas as pd

budget_account_list_base="DATASOURCE/budget_accounts.csv"
source='DATASOURCE/BACS.csv'
# Create your views here.
def budget(request):
    form_to_collect=budgetform(request.POST)
    if request.method=="POST":
          dataform=budgetform(request.POST)
          if dataform.is_valid():
            formdata=dataform
            #creating new dataframe from the data
            heads=['serial','economiccode','particuars','Type(Budget)']
            tabledata=[formdata.cleaned_data['serial'], formdata.cleaned_data['economiccode'], formdata.cleaned_data['particulars'],formdata.cleaned_data['account_type']]
            print(tabledata)
          else:
                print("false")
          df=pd.DataFrame([tabledata],columns=heads)
          print(df)
            #concatanation of data with existing data
          old_data=pd.read_csv(budget_account_list_base)
          print(old_data)
          new_data=pd.concat([old_data,df])
          new_data.to_csv(budget_account_list_base,index=False)
          print("here it is")

    else:
            new_data=pd.read_csv(budget_account_list_base)
            print(new_data)
    form=form_to_collect
    account_type=["Capital","Revenue"]
    data=pd.read_csv(budget_account_list_base)
    BACS=datareading(request)
    context={"budget_list":data.to_html(index=False),"form":form,"BACS":BACS,"type":account_type}
    return render(request,"budget.html",context)

def datareading(request):
  # Assuming 'source' is the path to your CSV file
  bacs = pd.read_csv(source)
  data_list=bacs["Name"].to_list()
 # Use key 'BACS' for consistency  # Optional, for debugging
  return data_list

