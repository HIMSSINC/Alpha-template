from django.db import models
from django.forms import ModelForm




class Lead(models.Model):
    job = models.CharField(max_length=100) # Ask for job title
    detail_1 = models.CharField(max_length=1000, blank=True) # All details of job
    detail_2 = models.CharField(max_length=1000, blank=True)
    detail_3 = models.CharField(max_length=1000, blank=True)
    detail_4 = models.CharField(max_length=1000, blank=True)
    detail_5 = models.CharField(max_length=1000, blank=True)
    detail_6 = models.CharField(max_length=1000, blank=True)
    detail_7 = models.CharField(max_length=1000, blank=True)
    urgency = models.CharField(max_length=100, blank=True)
    ready_to_hire = models.CharField(max_length=50, blank=True)
    custome_user_input = models.CharField(max_length=2000, blank=True)
    created = models.DateTimeField(auto_now_add=True) # anytime theres a new object the now time is set

    ############################################## Customer info #############################################

    zipcode = models.CharField(max_length=100, blank=True) # Most likly going to make a whole form in better detail
    street = models.CharField(max_length=1000, blank=True) # For the customers address
    customer_name = models.CharField(max_length=100, blank=True) # For customer full name
    customer_email = models.CharField(max_length=100, blank=True) # For customer email
    customer_phone = models.CharField(max_length=20, blank=True) # For Customers phone number


    def __str__(self): # So that we can see the name of something in our datebase
        return self.job
