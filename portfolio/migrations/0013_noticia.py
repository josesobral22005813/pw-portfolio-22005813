# Generated by Django 4.0.4 on 2022-06-09 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_post_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.CharField(max_length=500)),
                ('imagem', models.ImageField(null=True, upload_to='media/')),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
