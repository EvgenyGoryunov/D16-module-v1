# Generated by Django 4.0.3 on 2022-03-21 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0011_rename_notenote_response_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='note',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='main.note', verbose_name='id_объявления'),
        ),
        migrations.AlterField(
            model_name='response',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='id_пользователь'),
        ),
    ]
