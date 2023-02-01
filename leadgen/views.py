from django.shortcuts import render
from .models import Lead
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, LeadForm, BathroomForm, AcouticceilingForm1, AcouticceilingForm2, FlooringForm1, FlooringForm2, HomeBuilderForm1, HomeBuilderForm2, LandscapingForm1, LandscapingForm2, RoofingForm1, RoofingForm2, StoneTileForm1, StoneTileForm2, SwimmingpoolForm1, SwimmingpoolForm2
from django.utils import timezone
from formtools.wizard.views import SessionWizardView


def home(request):
    return render(request, 'home.html')

def acousticceilings(request):
    if request.method == 'GET':
        return render(request, 'bathroom.html', {'form':LeadForm()})
    
class multistepformsubmissionacousticceilings(SessionWizardView):
    template_name = 'acousticceilings.html'
    form_list =  [AcouticceilingForm1, AcouticceilingForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Acoustic Ceilings"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def bathroom(request):
    if request.method == 'GET':
        return render(request, 'bathroom.html', {'form':LeadForm()})
    
class multistepformsubmissionbathroom(SessionWizardView):
    template_name = 'bathroom.html'
    form_list =  [BathroomForm, LeadForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            detail_3 = form_data[1]['detail_3'], 
            zipcode = form_data[2]['zipcode'],
            customer_name = form_data[2]['customer_name'],
            customer_email = form_data[2]['customer_email'])

        new_lead.job = "Bathroom"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def flooring(request): ###
    if request.method == 'GET':
        return render(request, 'flooring.html', {'form':LeadForm()})
    
class multistepformsubmissionflooring(SessionWizardView):
    template_name = 'flooring.html'
    form_list =  [FlooringForm1, FlooringForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Flooring"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def homebuilder(request):
    if request.method == 'GET':
        return render(request, 'homebuilder.html', {'form':LeadForm()})
    
class multistepformsubmissionhomebuilder(SessionWizardView):
    template_name = 'homebuilder.html'
    form_list =  [HomeBuilderForm1, HomeBuilderForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Home builder"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def landscaping(request):
    if request.method == 'GET':
        return render(request, 'landscaping.html', {'form':LeadForm()})
    
class multistepformsubmissionlandscaping(SessionWizardView):
    template_name = 'landscaping.html'
    form_list =  [LandscapingForm1, LandscapingForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Landscaping"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def roofing(request):
    if request.method == 'GET':
        return render(request, 'roofing.html', {'form':LeadForm()})
    
class multistepformsubmissionroofing(SessionWizardView):
    template_name = 'roofing.html'
    form_list =  [RoofingForm1, RoofingForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Roofing"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def stonetile(request):
    if request.method == 'GET':
        return render(request, 'stonetile.html', {'form':LeadForm()})
    
class multistepformsubmissionstonetile(SessionWizardView):
    template_name = 'stonetile.html'
    form_list =  [StoneTileForm1, StoneTileForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Stone & Tile"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

def swimmingpool(request):
    if request.method == 'GET':
        return render(request, 'swimmingpool.html', {'form':LeadForm()})
    
class multistepformsubmissionswimmingpool(SessionWizardView):
    template_name = 'swimmingpool.html'
    form_list =  [SwimmingpoolForm1, SwimmingpoolForm2, UrgencyForm, ReadyToHireForm, CustomeUserInputForm, ContactForm]

    def done(self, form_list, **kwargs):
        form_data = [form.cleaned_data for form in form_list]
        new_lead = Lead(
            detail_1 = form_data[0]['detail_1'], 
            detail_2 = form_data[1]['detail_2'],
            urgency = form_data[2]['urgency'],
            ready_to_hire = form_data[3]['ready_to_hire'],
            custome_user_input = form_data[4]['custome_user_input'],
            zipcode = form_data[5]['zipcode'],
            customer_name = form_data[5]['customer_name'],
            customer_phone = form_data[5]['customer_phone'],
            street = form_data[5]['street'],
            customer_email = form_data[5]['customer_email'])

        new_lead.job = "Swimming pool"
        new_lead.save()

        return render(self.request, 'leadcompletion.html')

