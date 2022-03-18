from django.forms import ModelForm, TextInput, Textarea
from .models import Note


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        """задает название пустого поля"""
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        """__all__ - значит вывести все поля, exclude - исключает указанное поле
        widgets - переопределение размера вывода поля на страницу"""
        model = Note
        fields = '__all__'
        exclude = ['user']
        widgets = {'title': TextInput(attrs={'size': 98}), }
