from django.contrib import admin
from .models import linkType, businessArea, industry, Project, projectStatus

class adminBusinessArea( admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name','code')
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(businessArea, adminBusinessArea)

# ---------------------------------------------------------------------------------
class adminIndustry( admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name','code')
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(industry, adminIndustry)

# ---------------------------------------------------------------------------------
class adminLinkType( admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name','code')
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(linkType, adminLinkType)

# ---------------------------------------------------------------------------------
class adminProjectStatus( admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name','code')
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(projectStatus, adminProjectStatus)

# ---------------------------------------------------------------------------------
class adminProject( admin.ModelAdmin):
    list_display = ('name', 'business_area', 'industry')
    search_fields = ('name',)
    list_per_page = 12
    list_filter = ('name','business_area', 'industry')

admin.site.register(Project, adminProject)
