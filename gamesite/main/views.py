"""************************************************* ПРЕДСТАВЛЕНИЯ  ************************************************"""
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .filter import NoteFilter
from .forms import NoteForm, ResponseForm
from .models import Note


class NoteMain(ListView):
    """Главная страница, вывод в виде списка всех объявлений"""
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'
    ordering = ['-dateCreation']
    paginate_by = 5


class NoteCreate(CreateView):
    """Создание нового объявления"""
    template_name = 'note_create.html'
    form_class = NoteForm

    def form_valid(self, form):
        """Автозаполнение поля user"""
        form.instance.user = self.request.user
        return super().form_valid(form)


class NoteDelete(DeleteView):
    """Удаление объявления"""
    template_name = 'note_delete.html'
    queryset = Note.objects.all()
    # перенаправление на url с name = 'main'
    success_url = reverse_lazy('main')


class NoteDetail(DetailView):
    """Вывод подробностей объявления"""
    template_name = 'note_detail.html'
    queryset = Note.objects.all()
    form = ResponseForm
    # вариант2 добавления переменной в контекст шаблона
    extra_context = {'form': ResponseForm}

    def post(self, request, *args, **kwargs):
        form = ResponseForm(request.POST)
        print('111')
        if form.is_valid():
            form.instance.note_id = self.kwargs.get('pk')
            form.instance.user = self.request.user
            print('222')
            form.save()
            print('333')
            return redirect('main')


class NoteEdit(UpdateView):
    """Редактирование объявления"""
    template_name = 'note_edit.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        """Помогает извлечь у объекта нужное значение поля и сам объект"""
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)


class NoteSearch(ListView):
    """Фильтр и поиск объявлений"""
    model = Note
    template_name = 'note_search.html'
    context_object_name = 'note'
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


def add_response(request):
    # pk = request.GET.get('pk', )
    # print('Пользователь', request.user, 'добавлен в подписчики категории:', Category.objects.get(pk=pk))
    # Category.objects.get(pk=pk).subscribers.add(request.user)
    # return redirect('/news/')
    pass


def delete_response(request):
    # pk = request.GET.get('pk', )
    # print('Пользователь', request.user, 'удален из подписчиков категории:', Category.objects.get(pk=pk))
    # Category.objects.get(pk=pk).subscribers.remove(request.user)
    # return redirect('/news/')
    pass
