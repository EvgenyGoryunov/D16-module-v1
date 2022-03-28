from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput



class UserForm(forms.ModelForm):

    class Meta:
        """__all__ - значит вывести все поля, exclude - исключает указанное поле
        widgets/size - переопределение размера вывода поля на странице
        widgets/placeholder - текст в пустом поле"""
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {'username': TextInput(attrs={'size': 50, 'placeholder': 'Введите логин'}),
                   'first_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите имя'}),
                   'last_name': TextInput(attrs={'size': 50, 'placeholder': 'Введите фамилию'}),
                   'email': TextInput(attrs={'size': 50, 'placeholder': 'Введите почту'})}




# class UserForm(ModelForm):
    # """Форма для создания/редактирования нового объявления"""

    # def __init__(self, *args, **kwargs):
    #     """Задает название пустого (еще не выбранного) поля"""
    #     super().__init__(*args, **kwargs)
        # self.fields['category'].empty_label = 'Выберите категорию'


        # exclude = ['user']
        # задает форматирование полей
        # widgets = {'title': TextInput(attrs={'size': 98, 'placeholder': 'Название объявления'})}
