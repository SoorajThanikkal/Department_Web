from django.db import models
from public.models import Register
from django.db.models import Q
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class StudentProfile(models.Model):
    user = models.OneToOneField(Register,related_name = "student", on_delete = models.CASCADE,limit_choices_to=Q(is_student=True))
    register_no = models.PositiveIntegerField(validators = [MinValueValidator(10)],unique = True,blank=True,null = True)
    adm_no = models.PositiveIntegerField(validators = [MinValueValidator(5)], default=0)
    GENDER_CHOICES = (
        ('male', 'Male '),
        ('female', 'Female'),
    )
    gender =  models.CharField(max_length = 6, choices = GENDER_CHOICES,default = 'male')

    profile_pic = models.ImageField(upload_to = 'profile_photo/',default="../media/profile_photo/c-3.png",null=True)
    dob = models.DateField(blank = True, null = True)
    father_name = models.CharField(max_length = 15,  blank = True )
    mothers_name = models.CharField(max_length = 15, blank = True)
    

