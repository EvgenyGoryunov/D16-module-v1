from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView

from .forms import PostForm


class PostMain(View):
    def get(self, request):
        return HttpResponse(render(request, 'main.html', ))




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




class PostDelete(View):
    def get(self, request):
        return HttpResponse(render(request, 'post_delete.html', ))

class PostDetail(View):
    def get(self, request):
        return HttpResponse(render(request, 'post_detail.html', ))

class PostEdit(View):
    def get(self, request):
        return HttpResponse(render(request, 'post_edit.html', ))

class PostSearch(View):
    def get(self, request):
        return HttpResponse(render(request, 'post_search.html', ))



