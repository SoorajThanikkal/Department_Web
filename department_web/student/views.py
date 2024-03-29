from django.shortcuts import render, redirect
from .models import StudentProfile
from public.models import Register
from datetime import datetime


def StudentHomeView(request):
    return render(request,'studentindex.html ')
def StudentLoginView(request):
    from public.views import Role
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        users = Register.objects.filter(email = email , password = password, is_student = True)
        if users:
            user_data = Register.objects.get(email = email,password = password )
            id = user_data.id
            email = user_data.email
            password = user_data.password

            request.session['id'] = id
            request.session['email'] = email
            request.session['password'] = password
            return render(request,'studentindex.html')
        else:
            return Role(request)
    else:  
        return render(request,'signin.html')




def StdentProfileView(request):
    if 'email' in request.session:
        email = request.session['email']
        try:
            user = Register.objects.get(email=email)
            if user.is_teacher:
                return render(request,'signin.html')
            else:
                pass
            student_profile = StudentProfile.objects.filter(user=user).first()

            student_info = {
                'name': user.name,
                'email': user.email,
                'phone': user.phone,
                'address': user.address,
                'profile': student_profile
            }

            print("Student Info:", student_info)

            return render(request, 'userprofile.html', {'student_info': student_info})
        except Register.DoesNotExist:
            return render(request, 'studentindex.html')
    else:
        return render(request, 'studentindex.html')
    
    
    



def StudentProfileUpdateView(request):
    user_id = request.session.get('id')

    if user_id:
        user = Register.objects.filter(id=user_id).first()

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            if user:
                if name:
                    user.name = name
                if email:
                    user.email = email
                if phone:
                    user.phone = phone
                if address:
                    user.address = address
                user.save()

                return redirect('/student-profile/')

        return render(request, 'studentdetailsupdate.html', {'user': user})
    print("no data")

    
            
        
        

            


            

        