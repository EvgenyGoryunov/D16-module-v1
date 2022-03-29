from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import *

urlpatterns = [

    # path('registration/', UserRegistration.as_view(), name='registration'),

    path('profile/', UserProfile.as_view(), name='profile'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    # path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),

    path('signup/', BaseRegisterView.as_view(), name='signup'),

]
