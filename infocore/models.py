from django.db import models
from django.contrib.auth.models import User

# ---------------------------------------------------------------------------------
class industry(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Industry'
        verbose_name_plural = 'Industries'
        ordering = ['name']         
        managed = True
        db_table = 't_industry'
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class businessArea(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Business Area'
        verbose_name_plural = 'Business Areas'
        ordering = ['name']         
        managed = True
        db_table = 't_business_area'
    
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
    image_url = models.CharField(max_length=300, null=True, blank=True)
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

# ---------------------------------------------------------------------------------
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

