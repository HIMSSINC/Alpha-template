from django.db import models
from django.forms import ModelForm



class Lead(models.Model):
    job = models.CharField(max_length=100) # Ask for job title
    detail_1 = models.CharField(max_length=100, blank=True) # All details of job
    detail_2 = models.CharField(max_length=100, blank=True)
    detail_3 = models.CharField(max_length=100, blank=True)
    time_span = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True) # anytime theres a new object the now time is set
    # Customer info
    zipcode = models.CharField(max_length=100, blank=True) # Most likly going to make a whole form in better detail
    customer_name = models.CharField(max_length=100, blank=True) # For customer full name
    customer_email = models.CharField(max_length=100, blank=True) # For customer email


    def __str__(self): # So that we can see the name of something in our datebase
        return self.job
