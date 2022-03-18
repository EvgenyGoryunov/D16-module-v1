from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .forms import NoteForm
from .models import Note


class NoteMain(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'
    ordering = ['-dateCreation']
    # paginate_by = 5


class NoteCreate(CreateView):
    template_name = 'note_create.html'
    form_class = NoteForm

    def form_valid(self, form):
        """Автозаполнение поля user"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(DeleteView):
    """reverse_lazy('main') - перенаправление на представление с именем 'main'"""
    template_name = 'note_delete.html'
    queryset = Note.objects.all()
    success_url = reverse_lazy('main')


class NoteDetail(DetailView):
    template_name = 'note_detail.html'
    queryset = Note.objects.all()


class NoteEdit(UpdateView):
    template_name = 'note_edit.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)


class NoteSearch(ListView):
    def get(self, request):
        return HttpResponse(render(request, 'note_search.html', ))
    # pass
