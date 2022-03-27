from django.forms import ModelForm, TextInput, EmailInput
from .models import Note, Response


class NoteForm(ModelForm):
    """Форма для создания/редактирования нового объявления"""

    def __init__(self, *args, **kwargs):
        """Задает название пустого (еще не выбранного) поля"""
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Выберите категорию'

    class Meta:
        """__all__ - значит вывести все поля, exclude - исключает указанное поле
        widgets/size - переопределение размера вывода поля на странице
        widgets/placeholder - текст в пустом поле"""
        model = Note
        fields = '__all__'
        exclude = ['user']
        # задает форматирование полей
        widgets = {'title': TextInput(attrs={'size': 98, 'placeholder': 'Название объявления'})}


class ResponseForm(ModelForm):
    """Форма создания отклика"""

    class Meta:
        model = Response
        fields = ['content', ]
        widgets = {'content': TextInput(attrs={'size': 50, 'placeholder': 'Введите свои контакты'})}

