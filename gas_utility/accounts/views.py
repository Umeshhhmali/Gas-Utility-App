from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .models import UserLogin
from django.contrib.auth import authenticate


def register(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        confirm_password = request.POST.get('conf_password')
        role = request.POST.get('role')

        if not all([full_name, email, password, phone, address, confirm_password, role]):
            messages.error(request, "All fields are required!")
            return render(request, 'account.html')

        if UserLogin.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'account.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, 'account.html')
        user = UserLogin.objects.create(
            name=full_name,
            email=email,
            phone=phone,
            address=address,
            role=role  
        )
        user.set_password(password)
        user.save()

        messages.success(request, "Registration successful. Please log in.")
    return render(request, 'account.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        request.session['user_email'] = email
        request.session['user_password'] = password
        request.session.set_expiry(1209600)
        user = authenticate(request, email=email, password=password)  
        if user is not None and user.role == role:
            auth_login(request, user)
            return redirect('/dashboard/user')
        else:
            messages.error(request, "Invalid email or password.")
    return render(request, 'account.html')




    