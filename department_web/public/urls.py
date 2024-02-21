from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index ,name='index'),
    path('student-signup/', views.StudentSignup,name='signup-student'),
    path('teacher-signup/',views.TeacherSignup,name = 'teacher-signup'),
    path('role/',views.Role,name='choose-role'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)