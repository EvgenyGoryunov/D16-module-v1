from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .forms import PostForm
from .models import Post


class PostMain(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'  # (3)
    ordering = ['-dateCreation']
    # paginate_by = 5

class PostCreate(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'


class PostDelete(DeleteView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_delete.html', ))
    pass

class PostDetail(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()


class PostEdit(UpdateView):
    template_name = 'post_edit.html'
    form_class = PostForm
    success_url = '/'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)




class PostSearch(ListView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_search.html', ))
    pass



