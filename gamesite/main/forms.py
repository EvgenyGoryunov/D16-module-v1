from django import forms
from django.forms import ModelForm
from .models import Note


class NoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        """задает название пустого поля"""
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'

    class Meta:
        model = Note
        fields = '__all__'
        # widgets = {'user': forms.HiddenInput()}

        # fields = ['title',
        #           'content',
        #           'category',
        #           ]
        # вывод размеров полей
        # widgets = {'title': forms.TextInput({'class': 'form-input'}),
        #            'content': forms.Textarea({'cols': 500, 'rows': 100}),
        #            }
