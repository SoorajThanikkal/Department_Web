from django.urls import path

from .import views



urlpatterns = [
    
    path('teacher-index/',views.TeacherHomeView, name= 'teacher-home'),
    path('teacher-login/',views.TeacherLoginView,name='teacher-login'),
    path('student-view/',views.StudentDetailsView,name='student-deatils'),
    path('student-details-update/<id>',views.StudentEditView,name= 'student-details-update'),
    path('student-delete/<id>',views.DeleteStudentView,name='student-delete'),
    path('student-academic-update/<id>',views.StudentAcademicUpdateView,name='student-academic-update'),
    path('student-mark/<id>',views.add_subject_marks,name='student-mark'),
    path('student-attendance-c/',views.computer_student_attendance,name='Cstudent-att'),
    path('student-attendance-e/',views.electronic_student_attendance,name='Estudent-att'),
    
]