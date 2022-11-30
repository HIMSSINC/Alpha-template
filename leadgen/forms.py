from .models import Lead
from django.forms import ModelForm
from django import forms

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['detail_2','detail_3']


ZIPCODES = [
    ('Calabasas', 'Calabasas'), 
    ('Thousand Oaks', 'Thousand Oaks'), 
    ('Beverky hills','Beverky hills'),
    ]

BATHROOM_FIRST_DETAIL = [
    ('Sink', 'Sink'), 
    ('Countour', 'Countour'), 
    ('fridge','fridge'),
    ]

class BathroomForm(forms.Form):
        detail_1 = forms.CharField(widget=forms.RadioSelect(choices=BATHROOM_FIRST_DETAIL))
    

class ContactForm(forms.Form):
        customer_name = forms.CharField() 
        customer_email = forms.CharField()
        zipcode = forms.CharField()

    #     address = forms.CharField(
    #     max_length=100,
    #     widget=forms.Select(choices=ZIPCODES),
    # )
        





