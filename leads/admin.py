from django.contrib import admin
from .models import Lead, leadStatus
from django.views.decorators.clickjacking import xframe_options_sameorigin

class adminLeadStatus( admin.ModelAdmin):
    list_display = ('name', 'code' , )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(leadStatus, adminLeadStatus)

#-------------------------------------------------------------------------
class adminLead( admin.ModelAdmin):
    list_display = ('name', 'company', 'start_date', )
    search_fields = ('name','company',)
    list_per_page = 12
    list_filter = ('name','company')

admin.site.register(Lead, adminLead)

#-------------------------------------------------------------------------
