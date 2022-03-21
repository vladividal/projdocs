from django.db import models
from infocore.models import industry, businessArea

# ---------------------------------------------------------------------------------
class linkType(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Link Type'
        verbose_name_plural = 'Link Types'
        ordering = ['name']         
        managed = True
        db_table = 't_link_type'
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class projectStatus(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Project Status'
        verbose_name_plural = 'Project Status'
        ordering = ['name']         
        managed = True
        db_table = 't_project_status'
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Project Name')
    business_area = models.ForeignKey(businessArea, on_delete = models.CASCADE, verbose_name='Business Area')
    industry = models.ForeignKey(industry, on_delete = models.CASCADE, verbose_name='Industry') 
    project_url = models.CharField(max_length=500, verbose_name='Main Project URL')
    start_date = models.DateField(verbose_name='Start At')
    project_status = models.ForeignKey(projectStatus, on_delete = models.CASCADE, verbose_name='Project Status')
    end_date = models.DateField(verbose_name='Ended At')  
    budget_value = models.DecimalField(max_digits=15, decimal_places=2)   
    description = models.TextField(null=True, blank=True,verbose_name='Project descriprion')
    goals = models.TextField(null=True, blank=True,verbose_name='Expected Goals') 
    is_deleted = models.BooleanField(default=False)    
    inserted_at = models.DateTimeField(auto_now_add=True)    

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-start_date'] 
        managed = True
        db_table = 't_project'
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class projectModule(models.Model):
    project = models.ForeignKey(Project, on_delete = models.CASCADE, verbose_name='Project') 
    name = models.CharField(max_length=100,verbose_name='Module Name')
    description = models.TextField(null=True, blank=True,verbose_name='Module descriprion')
    sequence = models.IntegerField(verbose_name='Sequence')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Project Module'
        verbose_name_plural = 'Project Modules'
        ordering = ['name']         
        managed = True
        db_table = 't_project_module'
    
    def __str__(self):
        return self.name


