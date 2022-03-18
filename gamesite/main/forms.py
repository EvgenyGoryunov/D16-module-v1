from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        """задает название пустого поля"""
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        """__all__ - значит вывести все поля,
        exclude - исключает указанное поле"""
        model = Note
        fields = '__all__'
        exclude = ['user']