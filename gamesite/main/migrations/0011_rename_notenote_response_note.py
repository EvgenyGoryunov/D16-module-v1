# Generated by Django 4.0.3 on 2022-03-21 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_remove_response_note_response_notenote_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='response',
            old_name='notenote',
            new_name='note',
        ),
    ]
