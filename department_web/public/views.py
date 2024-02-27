from django.shortcuts import render
from .models import *
from teacher.models import Event
from student.views import StudentLoginView

# Create your views here.

def index(request):
    events = Event.objects.all()
    return render(request,'index.html', {'events': events})


def StudentSignup(request):
    if request.method == "POST":
        user = Register()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.is_student = True
        user.save()
        return StudentLoginView(request)
    return render(request, 'signup.html')

def TeacherSignup(request):
    if request.method == "POST":
        user = Register()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.phone = request.POST.get('phone')
        user.address = request.POST.get('address')
        user.is_teacher = True
        user.save()
        return StudentLoginView(request)
    return render(request, 'signup.html')

def Role(request):
    return render(request,'role.html')



