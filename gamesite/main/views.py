"""************************************************* ПРЕДСТАВЛЕНИЯ  ************************************************"""
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .filter import NoteFilter
from .forms import NoteForm, ResponseForm
from .models import *


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
    # queryset - переопределение вывода инфы на страницу
    queryset = Note.objects.all()
    # success_url - перенаправление на url с name = 'main'
    # reverse_lazy - ленивая переадресация, то есть выполняется после всего
    # выполнения всего кода, если просто reverse написать, то мгновенно переведет
    # не успев нижний код исполнить
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
            print('222')
            form.instance.note_id = self.kwargs.get('pk')
            print('333')
            form.instance.user = self.request.user
            form.save()

            # pk = self.kwargs.get('pk')
            # print('444', pk)
            # print('Пользователь', request.user, 'добавлен в подписчики категории:', Category.objects.get(pk=pk))
            # qaz = Note.objects.get(pk=pk)
            # qaz1 = Note.objects.get(pk=pk).user_response
            # print(qaz)
            # print(qaz1)
            """нужно получить id последнего отклика, из формы возможно или как???"""
            # print(Response)
            # print(Response.pk)
            # print(Response.user)
            # print(Response.content)

            # Note.objects.get(pk=pk).user_response.add(19)
            # добавить ид данного отклика в бд объявления в графу user_response
            print('555')

            return redirect('main')


def add_response(request):
    # pk = request.GET.get('pk', )
    # print('Пользователь', request.user, 'добавлен в подписчики категории:', Category.objects.get(pk=pk))
    # Category.objects.get(pk=pk).subscribers.add(request.user)
    # return redirect('/news/')
    pass


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
    ordering = ['-dateCreation']

    def get_context_data(self, **kwargs):
        """Для добавления новой переменной на страницу (filter)"""
        context = super().get_context_data(**kwargs)
        context['filter'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context


class ResponseList(ListView):
    """Страница отликов пользователя, вывод в виде списка"""
    template_name = 'user_response.html'
    context_object_name = 'notes'
    ordering = ['-dateCreation']
    paginate_by = 5

    def get_queryset(self):
        """Создает фильтр нужных объектов, здесь - по текущему пользователю"""
        user_id = self.request.user.id
        qaz = Note.objects.filter(user_id=user_id).values('id')
        print(qaz)
        print(type(qaz))
        # for i in qaz:
        #     print(type(i))
        #     x = int(i.values())
        #     print(i.values())
        #     print(x)



        # return Response.objects.filter(note_id=qaz)
        #
        #
        return Note.objects.filter(user_id=user_id)



    def get_context_data(self, **kwargs):
        user_id = self.request.user.id
        # print(Note.objects.filter(user_id=user_id).values('id'))
        context = super().get_context_data(**kwargs)
        context['responses'] = Response.objects.filter(user_id=user_id)
        # context['responses'] = Response.objects.all()
        # context['responses'] = NoteFilter(self.request.GET, queryset=self.get_queryset())
        return context
