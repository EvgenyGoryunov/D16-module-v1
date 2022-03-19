from django.forms import ModelForm, TextInput, Textarea
from .models import Note, Response


class NoteForm(ModelForm):
    """Форма для создания/редактирования нового объявления"""

    def __init__(self, *args, **kwargs):
        """задает название пустого (еще не выбранного) поля"""
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        """__all__ - значит вывести все поля, exclude - исключает указанное поле
        widgets - переопределение размера вывода поля на страницу"""
        model = Note
        fields = '__all__'
        exclude = ['user']
        widgets = {'title': TextInput(attrs={'size': 98}), }


class ResponseForm(ModelForm):
    """Форма создания отклика"""
    class Meta:
        model = Response
        fields = ['content']