from django.urls import path

from .views import *

urlpatterns = [
    path('', PostMain.as_view(), name='main'),
    path('create/', PostCreate.as_view(), name='create'),
    path('delete/', PostDelete.as_view(), name='delete'),
    path('detail/', PostDetail.as_view(), name='detail'),
    path('edit/', PostEdit.as_view(), name='edit'),
    path('search/', PostSearch.as_view(), name='search'),

    path('registration/', UserRegistration.as_view(), name='registration'),
    path('response/', UserResponse.as_view(), name='response'),
    path('profile/', UserProfile.as_view(), name='profile'),
]
