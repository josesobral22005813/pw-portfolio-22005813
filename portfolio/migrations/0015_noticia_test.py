# Generated by Django 4.0.4 on 2022-06-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0014_alter_noticia_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='test',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]