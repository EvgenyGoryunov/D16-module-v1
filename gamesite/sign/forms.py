from django.forms import TextInput
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class UserForm(forms.ModelForm):
    """Форма изменения данных пользователя"""
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        # fields = ("username",
        #           "first_name",
        #           "last_name",
        #           "email",
        #           "password1",
        #           "password2",)
        widgets = {'username': TextInput(attrs={'size': 50, 'placeholder': 'Введите логин'}),
                   'first_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите имя'}),
                   'last_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите фамилию'}),
                   'email': TextInput(attrs={'size': 50, 'placeholder': 'Введите почту'})}


class BaseRegisterForm(UserCreationForm):
    """Форма регистрации нового пользователя"""
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2",)

        # widgets = {'username': TextInput(attrs={'size': 50, 'placeholder': 'Введите логин'}),
        #            'first_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите имя'}),
        #            'last_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите фамилию'}),
        #            'email': TextInput(attrs={'size': 50, 'placeholder': 'Введите почту'})}


# class UserForm(ModelForm):
    # """Форма для создания/редактирования нового объявления"""

    # def __init__(self, *args, **kwargs):
    #     """Задает название пустого (еще не выбранного) поля"""
    #     super().__init__(*args, **kwargs)
        # self.fields['category'].empty_label = 'Выберите категорию'


        # exclude = ['user']
        # задает форматирование полей
        # widgets = {'title': TextInput(attrs={'size': 98, 'placeholder': 'Название объявления'})}
