from django import forms
from .import models
from .models import Event


class StudentAcademicModelForm(forms.ModelForm):
    class Meta:
        model = models.StudentAcademicModel
        fields = ['sem_details']
        


class SubjectMarkForm(forms.ModelForm):
    class Meta:
        model = models.SubjectMark
        fields = ['subject', 'semester', 'marks_obtained']
        
        
class InternalMarkForm(forms.ModelForm):
    class Meta:
        model = models.Internalmark
        fields = ['subject', 'assignment_marks', 'internal_marks']
        
class EventUploadForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'evimg']
        
        
