from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class NewProject(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length=255)
    startDate = models.DateField(auto_now_add=True)
    today = date.today()
    endDate = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta():
        verbose_name_plural = 'Projects'
    
    def __str__(self):
        return self.name
    
'''class AddiProject(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length=255)
    endDate = models.DateField()
    startDate = models.DateField(auto_now_add=True)
    today = date.today()
    #created_by = models.ForeignKey(User, on_delete=models.CASCADE)'''
    


