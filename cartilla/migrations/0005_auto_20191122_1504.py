# Generated by Django 2.2.7 on 2019-11-22 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartilla', '0004_auto_20191122_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartilla',
            name='leer_escribir',
            field=models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], default='SI', max_length=10, verbose_name='¿SABE LEER Y ESCRIBIR?'),
        ),
    ]
