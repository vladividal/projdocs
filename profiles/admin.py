from django.contrib import admin
from .models import Level, Profile, Account, Education, profileExperience, experienceCategory, profileSkills, profileSocialLinks, profileEducation, profileExperienceItens
from django.views.decorators.clickjacking import xframe_options_sameorigin

#-------------------------------------------------------------------------
class adminLevel( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(Level, adminLevel)

#-------------------------------------------------------------------------
class adminEducation( admin.ModelAdmin):
    list_display = ('account','education_title','education_level','institution_name','date_start','date_end','is_certification')
    search_fields = ('education_title','institution_name')
    list_per_page = 12
    list_filter = ('education_title','education_level','institution_name','is_certification')

    fieldsets = (
        (None, {
            'fields': ('account','education_level','education_title','institution_name','institution_url','description','is_certification')
        }),
        ('Datas Importantes', {
            'fields': ('date_start','date_end')
        }),
    )

admin.site.register(Education, adminEducation)

admin.site.register(experienceCategory)
admin.site.register(profileExperience)
admin.site.register(profileEducation)
admin.site.register(profileExperienceItens) 

#-------------------------------------------------------------------------
class InlineProfileSkills(admin.TabularInline):
    model = profileSkills
    fields = ('profile','skill')
    extra = 1

class InLineProfileExperience(admin.StackedInline):
#class InLineEducation(admin.TabularInline):
	model = profileExperience
	extra = 1

class InLineProfileSocialLinks(admin.TabularInline):
	model = profileSocialLinks
	extra = 1

class adminProfile( admin.ModelAdmin):
    list_display = ('title', 'role', 'level', 'is_active', 'is_your_main', 'updated_at' )
    search_fields = ('title','role',)
    list_per_page = 12
    list_filter = ('title','role')
    fields = ('account','title','banner','bio',('location','phone'),('email','website'),('language','role'),('level'),
    ('is_active', 'is_your_main'),'updated_at','tag' )

    inlines = [InlineProfileSkills, InLineProfileSocialLinks, InLineProfileExperience]

admin.site.register(Profile, adminProfile)






