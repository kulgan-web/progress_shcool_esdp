# Generated by Django 5.0.3 on 2024-05-11 13:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_group_options'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='teacher',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'teacher'}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_of_group', to=settings.AUTH_USER_MODEL, verbose_name='Учитель'),
        ),
    ]
