from django.db import models

class InsuranceCompany(models.Model):
    name = models.CharField(max_length=40)
    contact_phone = models.PositiveIntegerField(blank=True, null=True)
    contact_email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    
    def __str__(self):
        return self.name