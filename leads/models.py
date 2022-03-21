from django.db import models
from infocore.models import Skill, Role

# ---------------------------------------------------------------------------------
class Lead(models.Model):
    name = models.CharField(max_length=100,verbose_name='Lead Name')
    role = models.ForeignKey(Role, null=True, blank=True, on_delete = models.CASCADE, verbose_name='Role')    
    company = models.CharField(max_length=100,verbose_name='Company')
    contact = models.CharField(max_length=100, null=True, blank=True,verbose_name='Contact Name')
    email = models.CharField(max_length=100, null=True, blank=True,verbose_name='Email') 
    phone = models.CharField(max_length=300, null=True, blank=True,verbose_name='Phone')    
    start_date = models.DateField(verbose_name='Start Date') 
    description = models.TextField(null=True, blank=True,verbose_name='Lead Description')
    skill = models.ManyToManyField(Skill)  
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'
        ordering = ['-start_date']         
        managed = True
        db_table = 't_lead'

    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class leadActivity(models.Model):
    lead = models.ForeignKey(Lead, null=True, blank=True, on_delete = models.CASCADE, verbose_name='Lead') 
    title = models.CharField(max_length=100,verbose_name='Activity')
    activity_date = models.DateField(verbose_name='Activity Date')  
    contact = models.CharField(max_length=100, null=True, blank=True,verbose_name='Contact name')
    description = models.TextField(null=True, blank=True,verbose_name='Lead Description')
    action = models.CharField(max_length=100, null=True, blank=True,verbose_name='Action')
    action_date = models.DateField( null=True, blank=True, verbose_name='Date')
    action_detail = models.CharField(max_length=200, null=True, blank=True,verbose_name='Detail')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Lead Activities'
        verbose_name_plural = 'Lead Activity'
        ordering = ['-activity_date']         
        managed = True
        db_table = 't_lead_activity' 
    
    def __str__(self):
        return self.title