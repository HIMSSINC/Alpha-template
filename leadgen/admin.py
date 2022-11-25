from django.contrib import admin

from .models import Lead

class LeadAdmin(admin.ModelAdmin): # Allows us to edit admin and lets us create read only fleids
    readonly_fields = ('created',)

admin.site.register(Lead, LeadAdmin)
