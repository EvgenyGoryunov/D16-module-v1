from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import UserForm


class UserProfile(UpdateView):
    """Редактирование профиля пользователя"""
    template_name = 'user_profile.html'
    form_class = UserForm
    success_url = reverse_lazy('main')

    def get_object(self, **kwargs):
        """Помогает получить объект и вывести его на страницу"""
        user = self.request.user
        return User.objects.get(username=user)
