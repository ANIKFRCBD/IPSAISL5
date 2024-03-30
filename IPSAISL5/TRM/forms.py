from django import forms
class trmform(forms.Form):
    serial= forms.IntegerField(required= False)
    economiccode=forms.IntegerField(required= False)
    particulars=forms.CharField(max_length=128,required=False)
    unit=forms.IntegerField(required= False)
    amount=forms.IntegerField(required=False)