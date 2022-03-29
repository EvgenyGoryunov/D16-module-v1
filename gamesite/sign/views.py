from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from .forms import UserForm, BaseRegisterForm


class BaseRegisterView(CreateView):
    """Вывод формы для регистрации нового пользователя"""
    model = User
    template_name = 'signup.html'
    form_class = BaseRegisterForm
    success_url = reverse_lazy('login')


class UserProfile(UpdateView):
    """Редактирование профиля пользователя"""
    template_name = 'user_profile.html'
    form_class = UserForm
    success_url = reverse_lazy('main')

    def get_object(self, **kwargs):
        user = self.request.user
        return User.objects.get(username=user)
