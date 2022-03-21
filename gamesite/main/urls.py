from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
      path('', NoteMain.as_view(), name='main'),
      path('create/', NoteCreate.as_view(), name='create'),
      path('delete/<int:pk>', NoteDelete.as_view(), name='delete'),
      path('detail/<int:pk>/', NoteDetail.as_view(), name='detail'),
      path('edit/<int:pk>', NoteEdit.as_view(), name='edit'),
      path('search/', NoteSearch.as_view(), name='search'),
      path('ckeditor', include('ckeditor_uploader.urls')),
      # path('test/', Test, name='test'),
      # path('<int:pk>/add_response/', add_response, name='add_response'),
      # path('<int:pk>/delete_response/', delete_response, name='delete_response'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
