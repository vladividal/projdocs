from django.contrib import admin
from .models import Lead
from django.views.decorators.clickjacking import xframe_options_sameorigin

class adminLead( admin.ModelAdmin):
    list_display = ('name', 'company', 'start_date', )
    search_fields = ('name','company',)
    list_per_page = 12
    list_filter = ('name','company')

admin.site.register(Lead, adminLead)

#-------------------------------------------------------------------------
