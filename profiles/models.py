
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin 
from django.contrib.auth import get_user_model

from projdocs import settings


admin.site.site_header = 'ProjDocs Admin'
admin.site.site_title = 'ProjDocs Admin'
admin.site.index_title = 'ProjDocs Administration'

# ---------------------------------------------------------------------------------
class skillCategory(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Skill Category'
        verbose_name_plural = 'Skill Categories'
        ordering = ['name']         
        managed = True
        db_table = 't_skill_category'         
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Skill(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    skill_category = models.ForeignKey(skillCategory, default=2, on_delete = models.CASCADE, verbose_name='Category')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['name']         
        managed = True
        db_table = 't_skill'         
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Language(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['name']         
        managed = True
        db_table = 't_language'         

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Level(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Experience Level'        
        verbose_name_plural = 'Experience Levels'
        ordering = ['name']         
        managed = True
        db_table = 't_level' 

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class educationLevel(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Education Level'        
        verbose_name_plural = 'Education Levels'
        ordering = ['name']         
        managed = True
        db_table = 't_education_level' 

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Education(models.Model):
    education_level = models.ForeignKey(educationLevel, on_delete = models.CASCADE, verbose_name='Education Level')
    education_title = models.CharField(max_length=200, verbose_name='Title')
    institution_name = models.CharField(max_length=200, verbose_name='Institution Name')
    institution_url = models.CharField(max_length=500, verbose_name='Institution/Course URL')
    date_start = models.DateField(verbose_name='Start At')
    date_end = models.DateField(verbose_name='End At')  
    description = models.TextField(null=True, blank=True,verbose_name='Course descriprion')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_certification = models.BooleanField(default=False, verbose_name='Certification?')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Education '
        verbose_name_plural = 'Education'
        ordering = ['-date_start'] 
        managed = True
        db_table = 't_education'
    
    def __str__(self):
        return self.education_title

# ---------------------------------------------------------------------------------
class contractType(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)  
    inserted_at = models.DateTimeField(auto_now_add=True)  
    is_deleted = models.BooleanField(default=False)       

    class Meta:
        verbose_name = 'Contract Type'
        verbose_name_plural = 'Contract Types'
        ordering = ['name']         
        managed = True
        db_table = 't_contract_type'

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
CONTEXT_ACCOUNT_TYPE = (
    ('Free','Free'),
    ('Professional', 'Professional'),
    ('Premium', 'Premium'),    
    ('Trial', 'Trial'),    
)

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.CharField(max_length=300)
    account_type = models.CharField(max_length=30, choices=CONTEXT_ACCOUNT_TYPE, default='Free')
    is_active = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    observations = models.TextField(null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True, auto_now=False, editable=False)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
        ordering = ['-start_date']         
        managed = True
        db_table = 't_account'

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------

class experienceCategory(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)  
    inserted_at = models.DateTimeField(auto_now_add=True)    
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Experience Category'
        verbose_name_plural = 'Experience Categories'
        ordering = ['name']         
        managed = True
        db_table = 't_experience_category'

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------

class Role(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)  
    inserted_at = models.DateTimeField(auto_now_add=True)     
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Role'        
        verbose_name_plural = 'Roles'
        ordering = ['name']         
        managed = True
        db_table = 't_role'         

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------

class Tag(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)  
    inserted_at = models.DateTimeField(auto_now_add=True)   
    is_deleted = models.BooleanField(default=False)      

    class Meta:
        verbose_name = 'Tag'        
        verbose_name_plural = 'Tags'
        ordering = ['name']         
        managed = True
        db_table = 't_tags' 

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------

class socialNetwork(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=30)
    image_url = models.CharField(max_length=300)
    inserted_at = models.DateTimeField(auto_now_add=True)     
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Social Network'
        verbose_name_plural = 'Social Networks'
        ordering = ['name']         
        managed = True
        db_table = 't_social_network'         

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------

class Profile(models.Model):
    account = models.ForeignKey(Account, default=1, on_delete=models.CASCADE )     
    title = models.CharField(max_length=100)
    banner = models.CharField(max_length=300) 
    bio = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=300)
    website = models.CharField(max_length=300,blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE )
    role = models.ForeignKey(Role, on_delete=models.CASCADE ) 
    level= models.ForeignKey(Level, on_delete=models.CASCADE ) 
    tag = models.ManyToManyField(Tag, null=True, blank=True)
    is_active = models.BooleanField(default=False)
    is_your_main = models.BooleanField(default=False)
    updated_at = models.DateField()
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Professional Profile'
        verbose_name_plural = 'Profiles'
        ordering = ['-inserted_at']     
        managed = True
        db_table = 't_profile'  

    def __str__(self):
        return self.title

# ---------------------------------------------------------------------------------

class profileExperience(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE )
    experience_title = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200)
    company_url = models.CharField(max_length=300, null=True, blank=True)
    date_start = models.DateField()
    date_end = models.DateField(null=True, blank=True)
    contract_type = models.ForeignKey(contractType, on_delete=models.CASCADE )
    is_current = models.BooleanField(default=False)
    short_comments = models.TextField(null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Profile Experience'
        verbose_name_plural = 'Profile Experiences'
        ordering = ['-date_start'] 
        managed = True
        db_table = 't_profile_experience'
    
    def __str__(self):
        return self.experience_title      

# ---------------------------------------------------------------------------------

class profileExperienceItens(models.Model):
    profile_experience = models.ForeignKey(profileExperience, on_delete = models.CASCADE)
    item_description = models.TextField(null=True, blank=True)
    experience_category = models.ForeignKey(experienceCategory, on_delete=models.CASCADE )
    sequence = models.IntegerField()
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Profile Experience Item'
        verbose_name_plural = 'Profile Experiences Itens'
        ordering = ['sequence'] 
        managed = True
        db_table = 't_profile_experience_itens'
    
    def __str__(self):
        # alterar
        return '%s %s' % (self.experience_category , self.item_description)          

# ---------------------------------------------------------------------------------

class profileSocialLinks(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    social_network = models.ForeignKey(socialNetwork, on_delete=models.CASCADE )
    social_url = models.CharField(max_length=300)
    short_comments = models.TextField(null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Profile Social Link'
        verbose_name_plural = 'Profile Social Links'
        ordering = ['inserted_at'] 
        managed = True
        db_table = 't_profile_social_link'
    
    def __str__(self):
        return self.role

# ---------------------------------------------------------------------------------

class profileSkills(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE )
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Profile Skill'
        verbose_name_plural = 'Profile Skills'
        ordering = ['skill'] 
        managed = True
        db_table = 't_profile_skill'
    
 #   def __str__(self):
 #       return self.skill

# ---------------------------------------------------------------------------------

class profileEducation(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)    
    education_level = models.ForeignKey(educationLevel, on_delete = models.CASCADE)
    education_title = models.CharField(max_length=200)    
    institution_name = models.CharField(max_length=200)        
    institution_url = models.CharField(max_length=300)
    date_start = models.DateField()
    date_end = models.DateField()    
    description = models.TextField(null=True, blank=True)
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Profile Education'
        verbose_name_plural = 'Profile Education'
        ordering = ['date_start'] 
        managed = True
        db_table = 't_profile_education'
    
    def __str__(self):
        return self.education_title