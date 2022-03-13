from django.db import models

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
        ordering = ['name']         
        managed = True
        db_table = 't_lead'
    
    def __str__(self):
        return self.name