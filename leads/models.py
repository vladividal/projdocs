from django.db import models

# ---------------------------------------------------------------------------------
class leadStatus(models.Model):
    name = models.CharField(max_length=50,verbose_name='Name or description')
    code = models.CharField(max_length=10,verbose_name='Code')
    inserted_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)    

    class Meta:
        verbose_name = 'Lead Status'
        verbose_name_plural = 'Lead Status'
        ordering = ['name']         
        managed = True
        db_table = 't_lead_status' 
    
    def __str__(self):
        return self.name

# ---------------------------------------------------------------------------------
class Lead(models.Model):
    name = models.CharField(max_length=100,verbose_name='Lead Name')
    company = models.CharField(max_length=100,verbose_name='Company')
    start_date = models.DateField(verbose_name='Start Date') 
    description = models.TextField(null=True, blank=True,verbose_name='Lead Description')
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