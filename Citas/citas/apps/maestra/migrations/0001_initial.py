# Generated by Django 4.1.1 on 2022-10-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TablaMaestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tama_nombre1', models.CharField(max_length=30)),
                ('tama_nombre2', models.CharField(max_length=30)),
                ('tama_dependencia1', models.CharField(max_length=30)),
                ('tama_dependencia2', models.CharField(max_length=30)),
                ('tama_codigo', models.CharField(max_length=30)),
                ('tama_estado', models.CharField(max_length=30)),
            ],
        ),
    ]
