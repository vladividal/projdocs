from django.contrib import admin
from .models import Language, Role, Level, Tag, Profile, Skill, skillCategory, Account, Education, contractType, socialNetwork, profileExperience, educationLevel, experienceCategory, profileSkills, profileSocialLinks, profileEducation, profileExperienceItens
from django.views.decorators.clickjacking import xframe_options_sameorigin

class adminLanguage( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(Language, adminLanguage)

#-------------------------------------------------------------------------
class adminRole( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(Role, adminRole)

#-------------------------------------------------------------------------
class adminTag( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(Tag, adminTag)

#-------------------------------------------------------------------------
class adminSkill( admin.ModelAdmin):
    list_display = ('name', 'code', 'skill_category','inserted_at' )
    search_fields = ('name','skill_category','code',)
    list_per_page = 12
    list_filter = ('name','skill_category', 'code',)

admin.site.register(Skill, adminSkill)

#-------------------------------------------------------------------------
class adminSkillCategory( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(skillCategory, adminSkillCategory)

#-------------------------------------------------------------------------
class adminLevel( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(Level, adminLevel)

#-------------------------------------------------------------------------
class adminContractType( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(contractType, adminContractType)

#-------------------------------------------------------------------------
class adminSocialNetwork( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(socialNetwork, adminSocialNetwork)

#-------------------------------------------------------------------------
class adminEducationLevel( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(educationLevel, adminEducationLevel)

#-------------------------------------------------------------------------
class adminAccount( admin.ModelAdmin):
    list_display = ( 'name','last_name','email','account_type','start_date','is_active')
    search_fields = ('name','last_name','email',)
    list_per_page = 12
    list_filter = ('name','last_name','account_type')

    fieldsets = (
        (None, {
            'fields': ('user',('name','last_name'),'email','account_type','is_active')
        }),
        ('Datas Importantes', {
            'fields': ('start_date','end_date')
        }),
    )

admin.site.register(Account, adminAccount)

#-------------------------------------------------------------------------
class adminEducation( admin.ModelAdmin):
    list_display = ('education_title','education_level','institution_name','date_start','date_end','is_certification')
    search_fields = ('education_title','institution_name')
    list_per_page = 12
    list_filter = ('education_title','education_level','institution_name','is_certification')

    fieldsets = (
        (None, {
            'fields': ('education_level','education_title','institution_name','institution_url','description','is_certification')
        }),
        ('Datas Importantes', {
            'fields': ('date_start','date_end')
        }),
    )

admin.site.register(Education, adminEducation)

#-------------------------------------------------------------------------
class skillsInline(admin.TabularInline):
    model = profileSkills
    fields = ('profile','skill')
    extra = 1

class adminProfile( admin.ModelAdmin):
    list_display = ('title', 'role', 'level', 'is_active', 'is_your_main', 'updated_at' )
    search_fields = ('title','role',)
    list_per_page = 12
    list_filter = ('title','role')
    fields = ('account','title','banner','bio',('location','phone'),('email','website'),('language','role'),('level'),
    ('is_active', 'is_your_main'),'updated_at','tag' )

inLines = (skillsInline,)

admin.site.register(Profile, adminProfile)


#-------------------------------------------------------------------------
#admin.site.register(Profile)

admin.site.register(experienceCategory)
admin.site.register(profileExperience)
admin.site.register(profileSkills)
admin.site.register(profileSocialLinks)
admin.site.register(profileEducation)
admin.site.register(profileExperienceItens) 


