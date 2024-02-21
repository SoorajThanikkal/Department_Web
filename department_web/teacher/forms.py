from django import forms
from .import models


class StudentAcademicModelForm(forms.ModelForm):
    class Meta:
        model = models.StudentAcademicModel
        fields = ['sem_details']
        


class SubjectMarkForm(forms.ModelForm):
    class Meta:
        model = models.SubjectMark
        fields = ['subject', 'semester', 'marks_obtained']
        
        
