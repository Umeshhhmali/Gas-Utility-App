from django.urls import path
from . import views

urlpatterns = [ 
    path('user', views.user, name='user'),
    path('logout', views.logout_view, name='logout'),
    path('service', views.create_service_request, name='service'),
    
]