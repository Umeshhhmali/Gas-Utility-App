from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from .models import UserLogin  

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserLogin.objects.get(email=email)
            if check_password(password, user.password):  
                return user  
        except UserLogin.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return UserLogin.objects.get(pk=user_id)
        except UserLogin.DoesNotExist:
            return None
