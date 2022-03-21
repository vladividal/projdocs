from django.contrib import admin
from .models import Lead, leadActivity
from django.views.decorators.clickjacking import xframe_options_sameorigin

#-------------------------------------------------------------------------
class adminLead( admin.ModelAdmin):
    list_display = ('name', 'role', 'company', 'contact', 'email', 'phone', 'start_date')
    search_fields = ('name','company', 'contact')
    list_per_page = 12
    list_filter = ('name','company')

    fieldsets = (
        (None, {
            'fields': ('name','role', 'start_date','description')
        }),
        ('Contato', {
            'fields': ('company','contact',('email','phone'))
        }),
    )  

admin.site.register(Lead, adminLead)

#-------------------------------------------------------------------------
class adminLeadActivity( admin.ModelAdmin):
    list_display = ('lead', 'title', 'activity_date', 'contact', 'description', 'action', 'action_date', 'action_detail')
    search_fields = ('title', 'contact')
    list_per_page = 12
    list_filter = ('title','contact')

    fieldsets = (
        (None, {
            'fields': ('lead','title', 'activity_date','contact','description')
        }),
        ('Actions', {
            'fields': ('action','action_date','action_detail')
        }),
    ) 

admin.site.register(leadActivity, adminLeadActivity)