from django.shortcuts import render, redirect
from .models import ServiceRequest
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages
from accounts.models import UserLogin

def create_service_request(request):
    if request.method == "POST":
        service_type = request.POST.get("service_type")
        description = request.POST.get("description")
        status = request.POST.get("status", "pending")
        uploaded_file = request.FILES.get("file")

        file_path = None
        if uploaded_file:
            fs = FileSystemStorage()
            filename = fs.save(uploaded_file.name, uploaded_file)
            file_path = fs.url(filename)

        ServiceRequest.objects.create(
            user=request.user,
            service_type=service_type,
            description=description,
            status=status,
            file_path=file_path,
        )

        return redirect("/dashboard/user")
    return redirect("/dashboard/user")

def user(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            req = UserLogin.objects.get(email=request.user.email)
            serv = ServiceRequest.objects.all()
            print(serv)
            if request.user.role == 'admin':
                return render(request, 'admindash.html', {'req': req,'serv': serv})
            return render(request, 'userdash.html', {'req': req,'serv': serv})
        
        user_email = request.session.get('user_email') 
        user_password = request.session.get('user_password')
        if user_email and user_password:
            user = authenticate(request, email=user_email, password=user_password)
            if user is not None:
                auth_login(request, user)  
                req = UserLogin.objects.get(email=user_email)
                serv = ServiceRequest.objects.all()
                if request.user.role == 'admin':
                    return render(request, 'admindash.html', {'req': req,'serv': serv})
                return render(request, 'userdash.html', {'req': req,'serv': serv})
            else:
                messages.error(request, "Invalid email or password.")
        
    return redirect('/dashboard/user')

def logout_view(request):
    logout(request)
    return redirect('/accounts/login') 