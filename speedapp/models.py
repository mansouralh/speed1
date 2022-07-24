from django.db import models

# Create your models here.

class car ( models.Model): 
    color=models.CharField(max_length=10)
    
    def __str__(self):
        return self.color