# Generated by Django 3.2.3 on 2021-06-04 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('apelido', models.CharField(max_length=20)),
                ('telefone', models.IntegerField()),
                ('email', models.EmailField(max_length=64)),
                ('dataNasc', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='quizz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_1', models.CharField(max_length=2)),
                ('pergunta_2', models.CharField(max_length=2)),
                ('pergunta_3', models.CharField(max_length=2)),
                ('pergunta_4', models.CharField(max_length=2)),
                ('pergunta_5', models.CharField(max_length=15)),
                ('pergunta_6', models.CharField(max_length=15)),
                ('pergunta_7', models.CharField(max_length=15)),
                ('pergunta_8', models.CharField(max_length=2)),
                ('pergunta_9', models.CharField(max_length=2)),
                ('pergunta_10', models.CharField(max_length=2)),
            ],
        ),
    ]
