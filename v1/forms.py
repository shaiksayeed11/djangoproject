from django import forms
from django.db.models import fields
from django.forms.widgets import TextInput

GENDER_CHOICES = (
   ('','Select Gender'),
   ('Male', 'Male'),
   ('Female', 'Female'))

class PassForm(forms.Form):
    Pass_name= forms.CharField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Passenger Name'}),required=False)
    age= forms.IntegerField(widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Passenger Age'}),required=False)
    gender= forms.ChoiceField(choices=GENDER_CHOICES,widget= forms.Select(attrs={'class':'form-control'}),required=False)
     
