"""************************************************* ПРЕДСТАВЛЕНИЯ ************************************************"""
from django.core.mail import send_mail
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
    # queryset - переопределение вывода информации на страницу
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

    def get_context_data(self, **kwargs):
        """Функция для видимости поля откликов, поле не видимо если:
        1) я - автор объявления (самому себе отклик отправлять не нужно)
        2) уже отправил отклик на объявление ранее (два раза нельзя отправлять отклик на одно
        и тоже объявление, от спама и прочего)"""
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        note_author = Note.objects.get(id=pk).user

        # если ты автор объявления, то скрыть поле отклика
        if note_author == self.request.user:
            context['pole_response'] = False
            context['message_response'] = False
            context['edit_delete'] = True
        # если ты уже сделал отклик - поле отклика скрыть
        elif Response.objects.filter(user_response=self.request.user).filter(note=pk).exists():
            context['pole_response'] = False
            context['message_response'] = True
            context['edit_delete'] = False
        # если ты не автор объявления, и не сделал отклик - поле видимо
        else:
            context['pole_response'] = True
            context['message_response'] = False
            context['edit_delete'] = False

        return context

    def post(self, request, *args, **kwargs):
        """При отправки формы выполнить следующий код
        form.instance - для автоматического заполнения полей формы"""
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.instance.note_id = self.kwargs.get('pk')
            form.instance.user_response = self.request.user
            form.save()

            # если создан новый отклик, то автору письма отправить письмо-уведомление
            # получение нужных объектов из БД
            pk = self.kwargs.get('pk')
            user = f'{self.request.user.first_name} {self.request.user.last_name}'
            user_id = Note.objects.get(pk=pk).user_id
            note_title = Note.objects.get(pk=pk).title
            response_last_id = Response.objects.filter(user_response=self.request.user). \
                filter(note=pk).values('id')[0].get('id')
            response_content = Response.objects.get(pk=response_last_id).content
            response_time = Response.objects.get(pk=response_last_id).datetime

            # формирование письма автору объявления
            title = f'У вас новый отклик от {str(user)[:15]}'
            msg = f'На ваше объявление "{note_title}" пришел {str(response_time)[:19]} новый отклик от {user} ' \
                  f'следующего содержания: {response_content}'
            email = 'factoryskill@yandex.ru'
            note_email = User.objects.get(pk=user_id).email

            send_mail(subject=title, message=msg, from_email=email, recipient_list=[note_email, ])

            print("\n*************** ВЫВОД ПИСЬМА В КОНСОЛЬ (для удобства тестирования почты) *********************\n")
            print('Тема письма:', title)
            print('Контент письма:', msg)
            print('Адрес почты сервера:', email)
            print('Адрес отправления:', note_email)
            print("\n************************************ КОНЕЦ ПИСЬМА ********************************************\n")

            # волшебная ссылка перехода на ту же самую страницу после
            # выполнения POST-запроса, хвала stackoverflow.com
            return redirect(request.META.get('HTTP_REFERER'))


class NoteEdit(UpdateView):
    """Редактирование объявления"""
    template_name = 'note_edit.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        """Помогает получить объект и вывести его на страницу"""
        pk = self.kwargs.get('pk')
        return Note.objects.get(pk=pk)


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
    """Страница откликов пользователя
    выводит не наши отклики, а отклики на наши объявления"""
    template_name = 'user_response.html'
    context_object_name = 'responses'
    ordering = ['-datetime']
    paginate_by = 5

    def get_queryset(self, **kwargs):
        """Создает фильтры для вывода нужных объектов, 1 фильтр - по текущему пользователю
        то есть выводятся объявления только текущего пользователя, 2,3 фильтры - по статусу
        то есть еще не отклоненные/не принятые ранее отклики"""
        user_id = self.request.user.id
        # return Response.objects.all()
        return Response.objects.filter(note__user=user_id).filter(status_del=False).filter(status_add=False)

    def get_context_data(self, **kwargs):
        """Для добавления новых переменных на страницу
        filter - фильтрует отклики по объявлениям (форма выбора на странице)
        del_response - выводит отклоненные отклики (так, для удобства)
        add_response - выводит принятые отклики (так, для удобства)"""
        context = super().get_context_data(**kwargs)
        user_id = self.request.user.id
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        context['new_response'] = Response.objects. \
            filter(note__user=user_id).filter(status_del=False).filter(status_add=False)
        context['del_response'] = Response.objects.filter(note__user=user_id).filter(status_del=True)
        context['add_response'] = Response.objects.filter(note__user=user_id).filter(status_add=True)
        return context


class ResponseAccept(View):
    """Принятие отклика"""

    def get(self, request, *args, **kwargs):
        """Присваивает полю status_add значение = 1, то есть True, означает, что отклик
        принят, то есть он остается в бд, но больше не отображается в общем списке"""
        pk = self.kwargs.get('pk')
        resp = Response.objects.get(pk=pk)
        resp.status_add = 1
        resp.status_del = 0
        resp.save()

        # если отклик принят, то автору отклика отправить письмо-уведомление
        # получение нужных объектов из БД
        pk = self.kwargs.get('pk')
        user = f'{self.request.user.first_name} {self.request.user.last_name}'
        note_title = Note.objects.get(pk=Response.objects.get(pk=pk).note_id).title
        response_time = Response.objects.get(pk=pk).datetime

        # формирование письма автору отклика
        title = f'У вас одобренный отклик на объявление "{str(note_title)[:15]}"'
        msg = f'На ваш отклик от {str(response_time)[:19]} на объявление "{note_title}" пришло подтверждение'
        email = 'factoryskill@yandex.ru'
        response_email = User.objects.get(pk=Response.objects.get(pk=pk).user_response_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[response_email, ])

        print("\n*************** ВЫВОД ПИСЬМА В КОНСОЛЬ (для удобства тестирования почты) **********************\n")
        print('Тема письма:', title)
        print('Контент письма:', msg)
        print('Адрес почты сервера:', email)
        print('Адрес отправления:', response_email)
        print("\n************************************ КОНЕЦ ПИСЬМА ********************************************\n")

        return redirect('response')


class ResponseRemove(View):
    """Отклонение (условное удаление) отклика"""

    def get(self, request, *args, **kwargs):
        """Присваивает полю status_del значение = 1, то есть True, означает, что отклик
        отклонен, то есть он остается в бд, но больше не отображается в общем списке"""
        pk = self.kwargs.get('pk')
        qaz = Response.objects.get(id=pk)
        qaz.status_del = 1
        qaz.status_add = 0
        qaz.save()

        return redirect('response')
