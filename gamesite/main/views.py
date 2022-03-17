from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class PostMain(View):
    def get(self, request):
        return HttpResponse(render(request, 'main.html', ))

class PostCreate(View):
    def get(self, request):
        return HttpResponse(render(request, 'post_create.html', ))

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

class UserRegistration(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_registration.html', ))

class UserResponse(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_response.html', ))

class UserProfile(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_profile.html', ))


