from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .forms import NoteForm
from .models import Note


class NoteMain(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'  # (3)
    ordering = ['-dateCreation']
    # paginate_by = 5

class NoteCreate(CreateView):
    template_name = 'note_create.html'
    form_class = NoteForm
    # form = PostForm(request.POST)
    # if form.is_valid():
    #     response = form.save(commit=False)
    #     response.user = request.user
    #     response.save()
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
        # project = Project.objects.get(slug=self.kwargs['project_slug'])
        # form.instance.project = project
        # return super(ResponseCreate, self).form_valid(form)


class NoteDelete(DeleteView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'note_delete.html', ))
    pass

class NoteDetail(DetailView):
    template_name = 'note_detail.html'
    queryset = Note.objects.all()


class NoteEdit(UpdateView):
    template_name = 'note_edit.html'
    form_class = NoteForm

    # success_url = '/'
    # success_url = reverse('detail')
    # if
    #     success_url = reverse_lazy('main')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)



    # success_url = f'/detail/{self.kwargs.get("pk")}'
    # success_url = f'/detail/{id}'

    # def form_valid(self, form, **kwargs):
    #     id = self.kwargs.get('pk')
    #     if form.is_valid():
    #         form.save()
    #         return redirect('detail')
            # return redirect(f'/detail/{id}')
        # else:



        # return redirect('create')


        # if request.method == 'POST':
        #     form = PostForm(request.POST, instance=Post)
        #
        #     if form.is_valid():
        #         form.save()
        #
        #         return redirect('edit')
        # else:
        #     form = PostForm(instance=Post)





class NoteSearch(ListView):
    def get(self, request):
        return HttpResponse(render(request, 'note_search.html', ))
    # pass



