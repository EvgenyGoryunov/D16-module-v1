from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView

from .forms import PostForm
from .models import Post


class PostMain(ListView):
    model = Post
    template_name = 'main.html'
    context_object_name = 'posts'  # (3)
    ordering = ['-dateCreation']
    # paginate_by = 5

    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # вписываем наш фильтр в контекст, то есть чтоб переменная 'filter' появилась на странице
    #     context['filter'] = NewsFilter(self.request.GET, queryset=self.get_queryset())
    #     return context


    # def get(self, request):
    #     return HttpResponse(render(request, 'main.html', ))




class PostCreate(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    success_url = '/'


    # def get(self, request):
    #     return HttpResponse(render(request, 'post_create.html', ))



#
# class PostCreate(View):
#     def get(self, request):
#         return HttpResponse(render(request, 'post_create.html', ))
#




class PostDelete(DeleteView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_delete.html', ))
    pass

class PostDetail(DetailView):
    template_name = 'post_detail.html'
    queryset = Post.objects.all()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     id = self.kwargs.get('pk')
    #     qwe = Category.objects.filter(pk=Post.objects.get(pk=id).category.id).values("subscribers__username")
    #     context['is_not_subscribe'] = not qwe.filter(subscribers__username=self.request.user).exists()
    #     context['is_subscribe'] = qwe.filter(subscribers__username=self.request.user).exists()
    #     return context

    #
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_detail.html', ))

class PostEdit(UpdateView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_edit.html', ))
    pass

class PostSearch(ListView):
    # def get(self, request):
    #     return HttpResponse(render(request, 'post_search.html', ))
    pass



