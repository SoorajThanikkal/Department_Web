from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from public.models import Register
from django.shortcuts import get_object_or_404
from student.models import StudentProfile
from .models import StudentAcademicModel,ComputerAttendanceModel,ElectronicsAttendanceModel
from .forms import StudentAcademicModelForm,SubjectMarkForm
import datetime
from django.utils import timezone


# Create your views here.


def TeacherHomeView(request):
    return render(request, 'teacherhome.html')

def TeacherLoginView(request):
    from public.views import Role
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = Register.objects.filter(email = email , password = password, is_teacher = True)
        if users:
            user_data = Register.objects.get(email = email,password = password )
            id = user_data.id
            email = user_data.email
            password = user_data.password

            request.session['id'] = id
            request.session['email'] = email
            request.session['password'] = password
            return render(request,'teacherhome.html')
        else:
            return Role(request)
    else:  
        return render(request,'signin.html')
    
    
def StudentDetailsView(request):
    
    data = Register.objects.filter(is_student=True)
    
    student_info = {'data' : data}
    
    return render(request, 'viewstudents.html',student_info)


def StudentEditView(request, id):
    student = get_object_or_404(Register, id=id)
    student2, created = StudentProfile.objects.get_or_create(user=student)

    if request.method == 'POST':
        student.name = request.POST.get('name', student.name)
        student.email = request.POST.get('email', student.email)
        student.phone = request.POST.get('phone', student.phone)
        student.address = request.POST.get('address', student.address)

        student2.mothers_name = request.POST.get('mothers_name', student2.mothers_name)
        student2.father_name = request.POST.get('father_name', student2.father_name)
        register_no = request.POST.get('register_no')
        student2.register_no = int(register_no) if register_no is not None else None
        student2.adm_no = request.POST.get('adm_no', student2.adm_no)
        student2.gender = request.POST.get('gender', student2.gender)
        if 'profile_pic' in request.FILES:
            student2.profile_pic = request.FILES['profile_pic']
        dob = request.POST.get('dob', student2.dob)
        if dob:
            dob_formatted = datetime.datetime.strptime(dob, '%Y-%m-%d').date()
            student2.dob = dob_formatted

        student.save()
        student2.save()
        return redirect('/student-view/')

    return render(request, 'addstudentdetails.html', {'student': student, 'student2': student2})


def DeleteStudentView(request, id):
    student = get_object_or_404(Register, id=id)
    student_profile = get_object_or_404(StudentProfile, user=student)
    student_profile.delete()
    student.delete()
    return StudentDetailsView(request)


def StudentAcademicUpdateView(request, id):
    student = get_object_or_404(Register, id=id)
    student_academic, created = StudentAcademicModel.objects.get_or_create(student=student)

    if request.method == 'POST':
        form = StudentAcademicModelForm(request.POST, instance=student_academic)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('/student-view/', id=student.id)
    else:
        form = StudentAcademicModelForm(instance=student_academic)

    context = {
        'form': form,
        'student_academic': student_academic,
    }

    return render(request, 'addacademicdtls.html', context)



def add_subject_marks(request, id):
    student_academic = get_object_or_404(StudentAcademicModel, student__id=id)
    
    if request.method == 'POST':
        form = SubjectMarkForm(request.POST)
        if form.is_valid():
            subject_mark = form.save(commit=False)
            subject_mark.student_academic = student_academic
            subject_mark.save()
            return redirect('/student-view/', id=id)
    else:
        form = SubjectMarkForm()

    context = {
        'form': form,
        'student_academic': student_academic,
    }

    return render(request, 'add_subject_marks.html', context)


def computer_student_attendance(request):
    students = StudentAcademicModel.objects.filter(sem_details__course__course_name='computer')
    data = ComputerAttendanceModel()
    iso_date = timezone.now().date().isoformat()
    if request.method == 'POST':
        student_academic_id = request.POST.get('student_academic')
        date = request.POST.get('date')
        attendance_value = request.POST.get('attendance')
        attendance = True if attendance_value == 'on' else False
        print("Received date:", date)

        try:
            student_academic = StudentAcademicModel.objects.get(pk=student_academic_id)
            attendance_record = ComputerAttendanceModel(
                student_academic=student_academic,
                date=date,
                attendance=attendance
            )
            print("Date before saving:", attendance_record.date)
            attendance_record.save()
            print("Date after saving:", attendance_record.date)
            print("Attendance record saved successfully")
            return redirect('/teacher-index/')   
        except Exception as e:
            print(f"Error saving attendance record: {e}")
    
    
    student_info = {'students': students ,'data' : data ,'iso_date': iso_date}
    return render(request, 'addattendance.html', student_info)


def electronic_student_attendance(request):
    students = StudentAcademicModel.objects.filter(sem_details__course__course_name='electronics')
    data = ElectronicsAttendanceModel()
    iso_date = timezone.now().date().isoformat()
    if request.method == 'POST':
        student_academic_id = request.POST.get('student_academic')
        date = request.POST.get('date')
        attendance_value = request.POST.get('attendance')
        attendance = True if attendance_value == 'on' else False

        try:
            student_academic = StudentAcademicModel.objects.get(pk=student_academic_id)
            attendance_record = ElectronicsAttendanceModel(
                student_academic=student_academic,
                date=date,
                attendance=attendance
            )
            
            attendance_record.save()
            return redirect('/teacher-index/')  
        except Exception as e:
            print(f"Error saving attendance record: {e}")
    
    
    student_info = {'students': students ,'data' : data ,'iso_date': iso_date}
    return render(request, 'eleattendance.html', student_info)
    
    
        

        
    