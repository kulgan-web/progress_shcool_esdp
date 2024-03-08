# Generated by Django 5.0.2 on 2024-03-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagemodel',
            name='path',
            field=models.CharField(choices=[('/', 'Home'), ('/about_us/', 'About Us'), ('/courses/', 'Courses')], default='/', verbose_name='Путь до страницы'),
        ),
    ]
