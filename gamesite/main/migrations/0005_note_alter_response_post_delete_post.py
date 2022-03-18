# Generated by Django 4.0.3 on 2022-03-18 09:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0004_remove_post_cont_remove_post_cont_up_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Название')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Контент')),
                ('dateCreation', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.AlterField(
            model_name='response',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.note', verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
