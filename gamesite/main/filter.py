from django_filters import FilterSet, DateFromToRangeFilter
from .models import Note


class NoteFilter(FilterSet):
    # dateCreation = DateFromToRangeFilter()

    class Meta:
        model = Note
        fields = ('category', )
        # fields = ('user', 'category', 'dateCreation')
