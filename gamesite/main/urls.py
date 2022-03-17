from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
      path('', PostMain.as_view(), name='main'),
      path('create/', PostCreate.as_view(), name='create'),
      path('delete/', PostDelete.as_view(), name='delete'),
      path('detail/', PostDetail.as_view(), name='detail'),
      path('edit/', PostEdit.as_view(), name='edit'),
      path('search/', PostSearch.as_view(), name='search'),
      path('ckeditor', include('ckeditor_uploader.urls')),
  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
