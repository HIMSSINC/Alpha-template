from django.shortcuts import render
from .models import Lead
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactForm, LeadForm, BathroomForm
from django.utils import timezone
from formtools.wizard.views import SessionWizardView


def home(request):
    return render(request, 'home.html')

def bathroom(request):
    if request.method == 'GET':
        return render(request, 'bathroom.html', {'form':LeadForm()})
    
class multistepformsubmission(SessionWizardView):
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

    
