# Generated by Django 4.0.6 on 2022-08-06 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_classroom_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classroom',
            name='posts',
        ),
    ]
