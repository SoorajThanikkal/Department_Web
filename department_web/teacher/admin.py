from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(StudentAcademicModel)
admin.site.register(SubjectMark)
admin.site.register(ComputerAttendanceModel)
admin.site.register(ElectronicsAttendanceModel)
admin.site.register(Internalmark)
admin.site.register(Totalmark)



