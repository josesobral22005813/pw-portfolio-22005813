# Generated by Django 4.0.4 on 2022-05-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_pontuacaoquizz'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autor', models.CharField(max_length=200)),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=200)),
                ('data', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
