
from django.db import models
from public.models import Register
from student.models import StudentProfile
from django.utils import timezone
from django.db.models import Q


# Create your models here.
    
    
class TeacherProfileClass(models.Model):
    user = models.OneToOneField(Register,related_name = "teacher", on_delete = models.CASCADE,limit_choices_to=Q(is_teacher=True))
    
    
class Course(models.Model):
    course_name = models.CharField(max_length = 100)
    def __str__(self):
        return self.course_name
    
class Subject(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Semester(models.Model):
    number = models.IntegerField(null = True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.course} - Semester {self.number}'
    class Meta:
        unique_together = ('number', 'course')
    
    
class StudentAcademicModel(models.Model):
    student = models.OneToOneField(Register, on_delete = models.CASCADE,limit_choices_to=Q(is_student=True))
    sem_details = models.ForeignKey(Semester, on_delete=models.CASCADE,null =True)
    
    def __str__(self):
        return f'{self.student.name} '
    
    
    
class SubjectMark(models.Model):
    student_academic = models.ForeignKey(StudentAcademicModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    marks_obtained = models.FloatField(default=0.0)
    def __str__(self):
        return f"{self.subject} - {self.student_academic} - {self.marks_obtained}"
    
    
class ComputerAttendanceModel(models.Model):
    student_academic = models.ForeignKey(StudentAcademicModel, on_delete=models.CASCADE,null = True)
    date = models.DateField(default = timezone.now().date())
    attendance = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date} - {self.student_academic}"
    
class ElectronicsAttendanceModel(models.Model):
    student_academic = models.ForeignKey(StudentAcademicModel, on_delete=models.CASCADE,limit_choices_to=Q(sem_details__course__course_name ='electronics'))
    date = models.DateField()
    attendance = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.date} - {self.student_academic}"
    
    # models.py



class Internalmark(models.Model):
    student_academic = models.ForeignKey(StudentAcademicModel, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignment_marks = models.FloatField(default=0.0)
    internal_marks = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student_academic} - {self.subject}"
    
class Totalmark(models.Model):
    student_academic = models.ForeignKey(StudentAcademicModel, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE,null = True)
    total_marks = models.FloatField(default=0.0, null=True, blank=True)


    def __str__(self):
        return f"{self.semester} - {self.total_marks}"
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    evimg = models.ImageField(upload_to='event-photo/', blank=True)
     



    
    

    

    
    

    

    
    

    
    

   