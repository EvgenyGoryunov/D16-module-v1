from django.urls import path

from .views import *

urlpatterns = [

    # path('registration/', UserRegistration.as_view(), name='registration'),
    path('profile/', UserProfile.as_view(), name='profile'),

]
