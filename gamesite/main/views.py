"""************************************************* ПРЕДСТАВЛЕНИЯ ************************************************"""
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .filter import NoteFilter, ResponseFilter
from .forms import NoteForm, ResponseForm
from .models import *


class NoteMain(ListView):
    """Главная страница, вывод в виде списка всех объявлений"""
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'
    ordering = ['-datetime']
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
    # queryset - переопределение вывода инфы на страницу
    queryset = Note.objects.all()
    # success_url - перенаправление на url с name = 'main'
    success_url = reverse_lazy('main')


class NoteDetail(DetailView):
    """Вывод подробностей объявления"""
    template_name = 'note_detail.html'
    queryset = Note.objects.all()
    form = ResponseForm
    # вариант2 добавления переменной в контекст шаблона
    extra_context = {'form': ResponseForm}

    def post(self, request, *args, **kwargs):
        """При отправки формы выполнить след код
        form.instance - для автоматического заполнения полей"""
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.instance.note_id = self.kwargs.get('pk')
            form.instance.user_author = Note.objects.get(id=self.kwargs.get('pk')).user.id
            form.instance.user_response = self.request.user
            first_name = self.request.user.first_name
            last_name = self.request.user.last_name
            fio = first_name + " " + last_name
            form.instance.user_fio = fio
            form.save()

            return redirect('main')


class NoteEdit(UpdateView):
    """Редактирование объявления"""
    template_name = 'note_edit.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        """Помогает получить объект и вывести его на страницу"""
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)


class NoteSearch(ListView):
    """Фильтр и поиск объявлений"""
    model = Note
    template_name = 'note_search.html'
    context_object_name = 'note'
    ordering = ['-datetime']

    def get_context_data(self, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ResponseList(ListView):
    """Страница отликов пользователя
    выводит не наши отклики, а отклики на наши объявления"""
    template_name = 'user_response.html'
    context_object_name = 'responses'
    ordering = ['-datetime']
    paginate_by = 5

    def get_queryset(self, **kwargs):
        """Создает фильтры нужных объектов, 1 фильтр - по текущему пользователю
        то есть выводятся объявления только текущего пользователя, 2 фильтр - по статусу
        то есть еще не отклоненные ранее отклики"""
        user_id = self.request.user.id
        print(user_id)
        print('11111111111111')
        # print(Response.objects.get(note__id=8).title[:1])
        # print(Response.objects.filter(note_id__user_id=user_id).filter(status=False))
        print('**********************************************')
        return Response.objects.filter(note__user=user_id)
        # return Response.objects.filter(note__id=user_id)
        # return Response.objects.filter(user_note=user_id).filter(status=False)

    def get_context_data(self, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ResponseAccept(View):
    """Принятие отклика"""

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get('pk')
        print('id', id)
        print('********************1111*********************')
        return redirect('response')


class ResponseRemove(View):
    """Отклонение (условное удаление) отклика"""

    def get(self, request, *args, **kwargs):
        """Присваивает полю status значение = 1, то есть True, означает, что отклик
        отклонен, то есть он остается в бд, но больше не отображается в общем списке"""
        id = self.kwargs.get('pk')
        qaz = Response.objects.get(id=id)
        qaz.status = 1
        qaz.save()

        return redirect('response')
