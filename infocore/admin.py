from django.contrib import admin
from .models import Language, Skill, skillCategory, socialNetwork, educationLevel, Role, Tag, contractType, Account

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
class adminContractType( admin.ModelAdmin):
    list_display = ('name', 'code', 'inserted_at' )
    search_fields = ('name','code',)
    list_per_page = 12
    list_filter = ('name','code')

admin.site.register(contractType, adminContractType)

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
