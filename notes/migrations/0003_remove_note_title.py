# Generated by Django 5.1.5 on 2025-02-05 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_note_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='title',
        ),
    ]
