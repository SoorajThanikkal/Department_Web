from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator

# Create your models here.    

class Register(models.Model):
    name = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=8)
    phone = models.CharField(max_length=15, validators=[MaxLengthValidator(15), MinLengthValidator(0)], default='', null=True, blank=True)
    address = models.TextField(max_length=255, null=True)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    
    def __str__(self):
        return str(self.name)
    
    

    

    

    
    
    



    

    



