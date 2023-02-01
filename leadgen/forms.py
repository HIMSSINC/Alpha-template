from .models import Lead
from django.forms import ModelForm
from django import forms

class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['detail_2','detail_3']


####################################### Basic forms that apply to every lead #######################################

class ContactForm(forms.Form):
    customer_name = forms.CharField(required=False) 
    customer_email = forms.CharField(required=False)
    customer_phone = forms.CharField(required=False)
    zipcode = forms.CharField(required=False)
    street = forms.CharField(required=False)



URGENCY_DETAIL = [
    ('As soon as possible','As soon as possible'),
    ('1-2 weeks','1-2 weeks'),
    ('2-4 weeks','2-4 weeks'),
    ('More than 4 weeks','More than 4 weeks'),
]

class UrgencyForm(forms.Form):
    urgency = forms.CharField(label="When would you like this request to be completed?", widget=forms.RadioSelect(choices=URGENCY_DETAIL))

READY_TO_HIRE = [
    ('Ready to hire', 'Ready to hire'),
    ('Planning & Budgeting', 'Planning & Budgeting'),
]

class ReadyToHireForm(forms.Form):
    ready_to_hire = forms.CharField(label="Choose the appropriate status for this project", widget=forms.RadioSelect(choices=READY_TO_HIRE))

class CustomeUserInputForm(forms.Form):
    custome_user_input = forms.CharField(label="Anything else you'd like to tell us?", required=False, widget=forms.Textarea)


####################################### Start of all the lead Forms and their options in Alphabtical order #######################################


ACOUSTICCEILING_FIRST_DETAIL = [
    ('New construction/Addition', 'New construction/Addition'),
    ('Replacing old ceiling','Replacing old ceiling'),
]

ACOUSTICCEILING_SECOND_DETAIL = [
    ('Standard', 'Standard'),
    ('Designer', 'Designer'),
    ('Sound absorbing', 'Sound absorbing'),
    ('Insulation', 'Insulation'),
    ('Fire rated', 'Fire rated'),
]

ACOUSTICCEILING_THIRD_DETAIL = [
    ('Ready to hire', 'Ready to hire'),
    ('Planning & Budgeting', 'Planning & Budgeting'),
]

class AcouticceilingForm1(forms.Form):
    detail_1 = forms.CharField(label="Why do you need to install a new ceiling?", widget=forms.RadioSelect(choices=ACOUSTICCEILING_FIRST_DETAIL))

class AcouticceilingForm2(forms.Form):
    detail_2 = forms.CharField(label="What are the specific characteristics you are looking for?", widget=forms.RadioSelect(choices=ACOUSTICCEILING_SECOND_DETAIL)) 



BATHROOM_FIRST_DETAIL = [
    ('Sink', 'Sink'), 
    ('Countour', 'Countour'), 
    ('fridge','fridge'),
    ]

class BathroomForm(forms.Form):
    detail_1 = forms.CharField(widget=forms.RadioSelect(choices=BATHROOM_FIRST_DETAIL))
    


FLOORING_FIRST_DETAIL = [
    ('Install or replace flooring','Install or replace flooring'),
    ('Repair existing flooring','Repair existing flooring'),
    ('Refinish existing wood flooring','Refinish existing wood flooring'),
]

FLOORING_SECOND_DETAIL = [
    ('Carpet','Carpet'),
    ('Hardwood','Hardwood'),
    ('Laminate','Laminate'),
    ('Natural stone','Natural stone'),
    ('Vinyl','Vinyl'),
    ('Ceramic','Ceramic'),
]

class FlooringForm1(forms.Form):
    detail_1 = forms.CharField(label="What type of flooring project is this?",widget=forms.RadioSelect(choices=FLOORING_FIRST_DETAIL))

class FlooringForm2(forms.Form):
    detail_2 = forms.CharField(label="Select th type of flooring material you want",widget=forms.RadioSelect(choices=FLOORING_SECOND_DETAIL))



HOMEBUILDER_FIRST_DETAIL = [
    ('Build a custome home','Build a custome home'),
    ('Home inspection','Home inspection'),
]

HOMEBUILDER_SECOND_DETAIL = [
    ('Yes','Yes'),
    ('No','No'),
    ('Maybe','Maybe'),
]

class HomeBuilderForm1(forms.Form):
    detail_1 = forms.CharField(label="What kind of home building project is this?",widget=forms.RadioSelect(choices=HOMEBUILDER_FIRST_DETAIL))

class HomeBuilderForm2(forms.Form):
    detail_2 = forms.CharField(label="Are you looking to build a modular home?",widget=forms.RadioSelect(choices=HOMEBUILDER_SECOND_DETAIL))



LANDSCAPING_FIRST_DETAIL = [
    ('Design new landscape','Design new landscape'),
    ('Install or replace landscaping','Install or replace landscaping'),
    ('Lawn Care','Lawn Care'),
    ('Sprinkler system','Sprinkler system'),
    ('Trees & Shrubs','Trees & Shrubs'),
    ('Install or repair outdoor lighting','Install or repair outdoor lighting'),
    ('Other','Other'),
]

LANDSCAPING_SECOND_DETAIL = [
    ('New Landscaping from bare dirt','New Landscaping from bare dirt'),
    ('Completely replace exisitng landscape','Completely replace exisitng landscape'),
    ('Updating existing landscape','Updating existing landscape'),
]

class LandscapingForm1(forms.Form):
    detail_1 = forms.CharField(label="What type of landscaping project is this?",widget=forms.RadioSelect(choices=LANDSCAPING_FIRST_DETAIL))

class LandscapingForm2(forms.Form):
    detail_2 = forms.CharField(label="What is the nature of this landscaping project?",widget=forms.RadioSelect(choices=LANDSCAPING_SECOND_DETAIL))



ROOFING_FIRST_DETAIL = [
    ('Completely replace roof','Completely replace roof'),
    ('Install roof on new construction','Install roof on new construction'),
    ('Repair existing roof','Repair existing roof'),
    ('Clean a roof','Clean a roof'),
    ('Apply roof sealant','Apply roof sealant'),
    ('Install roof heating cable to melt snow','Install roof heating cable to melt snow'),
    ('Awnigs or Patio Covers','Awnigs or Patio Covers'),
    ('Roof inspection','Roof inspection'),
]

ROOFING_SECOND_DETAIL = [
    ('Asphalt','Asphalt'),
    ('Flat, Foam or Single Ply','Flat, Foam or Single Ply'),
    ('Metal','Metal'),
    ('Natural Slate','Natural Slate'),
    ('Wood Shake/Composite','Wood Shake/Composite'),
    ('Tile','Tile'),
]

class RoofingForm1(forms.Form):
    detail_1 = forms.CharField(label="What type of roofing project is this?",widget=forms.RadioSelect(choices=ROOFING_FIRST_DETAIL))

class RoofingForm2(forms.Form):
    detail_2 = forms.CharField(label="Select the type of roofing material you want",widget=forms.RadioSelect(choices=ROOFING_SECOND_DETAIL))



STONETILE_FIRST_DETAIL = [
    ('Install Ceramic or Porcelain Tile','Install Ceramic or Porcelain Tile'),
    ('Repair Ceramic or Porcelain Tile','Repair Ceramic or Porcelain Tile'),
    ('Repair Natural Stone Tile','Repair Natural Stone Tile'),
    ('Install or Repair Tile','Install or Repair Tile'),
    ('Clean & Seal Grout or Tile','Clean & Seal Grout or Tile'),
    ('Replace or Repair Grout','Replace or Repair Grout'),
    ('Clean, Grout, Polish and Maintain Tile, Stone or Marble','Clean, Grout, Polish and Maintain Tile, Stone or Marble'),
    ('Natural Stone REstoration & Polishing','Natural Stone REstoration & Polishing'),
    ('Install Glass Blocks','Install Glass Blocks'),
]

STONETILE_SECOND_DETAIL = [
    ('Replace existing tile','Replace existing tile'),
    ('Replace existing non-tile surface','Replace existing non-tile surface'),
    ('Tile for new construction','Tile for new construction'),
]

class StoneTileForm1(forms.Form):
    detail_1 = forms.CharField(label="What type of stone & tile project is this?",widget=forms.RadioSelect(choices=STONETILE_FIRST_DETAIL))

class StoneTileForm2(forms.Form):
    detail_2 = forms.CharField(label="What kind of project is this?",widget=forms.RadioSelect(choices=STONETILE_SECOND_DETAIL))



SWIMMINGPOOL_FIRST_DETAIL = [
    ('New inground pool','New inground pool'),
    ('New above ground pool','New above ground pool'),
    ('Pool repair, remodel or maintenance','Pool repair, remodel or maintenance'),
    ('Hot tub or spa install, replace or repair','Hot tub or spa install, replace or repair'),
    ('Sauna install, replace or repair','Sauna install, replace or repair'),
    ('Pool heater install, replace or repair','Pool heater install, replace or repair'),
    ('Pool opening or closing service','Pool opening or closing service'),
]

SWIMMINGPOOL_SECOND_DETAIL = [
    ('Custome Pool','Custome Pool'),
    ('Fiberglass','Fiberglass'),
    ('Vinyl','Vinyl'),
]

class SwimmingpoolForm1(forms.Form):
    detail_1 = forms.CharField(label="What type of pool project is this?",widget=forms.RadioSelect(choices=SWIMMINGPOOL_FIRST_DETAIL))

class SwimmingpoolForm2(forms.Form):
    detail_2 = forms.CharField(label="What type of pool would you like installed?",widget=forms.RadioSelect(choices=SWIMMINGPOOL_SECOND_DETAIL))



