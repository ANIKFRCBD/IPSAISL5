from django import forms

class budget(forms.Form):
    serial= forms.IntegerField(required= False)
    economiccode=forms.IntegerField(required= True)
    particulars=forms.CharField(max_length=128,required=False)
    account_type=forms.CharField(max_length=128,required=True)