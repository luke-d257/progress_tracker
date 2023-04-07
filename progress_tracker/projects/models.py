from django.db import models

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(max_length=255)
    date = models.DateField(auto_now_add=True)
    percOfComp = models.IntegerField()
    idealPerc = models.IntegerField()

    #class Meta():
    #    verbose_plural_name = 'Projects'
    
    def __str__(self):
        return self.name

