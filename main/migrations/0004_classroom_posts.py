# Generated by Django 4.0.6 on 2022-08-06 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_classroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='posts',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.post'),
        ),
    ]
