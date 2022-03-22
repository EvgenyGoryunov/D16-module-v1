from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Модель - категории"""
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')

    def __str__(self):
        """Вид отображения модели в панели управления"""
        return f'{self.name}'


class Note(models.Model):
    """Модель - объявления
    поле контент может содержать текст, фото, видео, документы
    поле user авто присваивает значение текущего пользователя"""
    title = models.CharField(max_length=128, verbose_name='Название')
    content = RichTextUploadingField(verbose_name='Контент')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, verbose_name='Пользователь')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    # response = models.

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        """Функция перенаправления пользователя после успешного добавления или изменения в бд
        в данном случае - обратиться к url с именем detail, передав pk = id, и далее по списку..."""
        return reverse('detail', kwargs={'pk': self.id})


class Response(models.Model):
    """Модель - отклики"""
    note = models.ForeignKey(Note, on_delete=models.CASCADE, verbose_name='id_объявления')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='id_пользователь')
    content = models.TextField(verbose_name='Контент')
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'{self.user}'
