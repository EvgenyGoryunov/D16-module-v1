from django.urls import path

from .views import *

urlpatterns = [

    path('registration/', UserRegistration.as_view(), name='registration'),
    path('response/', UserResponse.as_view(), name='response'),
    path('profile/', UserProfile.as_view(), name='profile'),

]
