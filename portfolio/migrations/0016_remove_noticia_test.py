# Generated by Django 4.0.4 on 2022-06-09 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0015_noticia_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='test',
        ),
    ]