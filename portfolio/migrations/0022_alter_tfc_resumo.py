# Generated by Django 4.0.4 on 2022-06-17 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0021_alter_tecnologia_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tfc',
            name='resumo',
            field=models.CharField(max_length=1000),
        ),
    ]
