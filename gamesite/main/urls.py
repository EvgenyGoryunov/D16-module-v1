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
      path('response/', ResponseList.as_view(), name='response'),
      path('response_remove/', ResponseRemove.as_view(), name='remove'),
      path('response_accept/', ResponseAccept.as_view(), name='accept'),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
