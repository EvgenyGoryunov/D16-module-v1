from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """Модель - категории"""
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    """Модель - объявления
     поле контент может содержать текст, фото, видео, документ"""
    title = models.CharField(max_length=128, verbose_name='Название')
    content = models.TextField(verbose_name='Контент')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    def __str__(self):
        return f'{self.title}'


class Response(models.Model):
    """Модель - отклики"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Название')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    content = models.TextField(verbose_name='Контент')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user}'
