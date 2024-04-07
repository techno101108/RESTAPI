from django.db import models

class Drink(models.Model):
    name= models.CharField(max_length=300)
    description=models.CharField(max_length=500)
    created_at=models.DateTimeField(auto_now_add=True,null=False,blank=False)
    updated_at=models.DateTimeField(auto_now=True,null=False,blank=False)
    
    def __str__(self) -> str:
        return self.name