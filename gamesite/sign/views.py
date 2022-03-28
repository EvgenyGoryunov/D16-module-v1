from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class UserRegistration(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_registration.html', ))


class UserResponse(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_response.html', ))


class UserProfile(View):
    def get(self, request):
        return HttpResponse(render(request, 'user_profile.html', ))
