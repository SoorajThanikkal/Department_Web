from django.urls import path
from .import views


urlpatterns = [
    path('student-login/',views.StudentLoginView,name='student-login'),
    path('student-profile/',views.StdentProfileView,name = 'student-profile'),
    path('student-home/',views.StudentHomeView, name = 'student-home'),
    path('student-profile-update/',views.StudentProfileUpdateView, name = 'student-profile')
]

