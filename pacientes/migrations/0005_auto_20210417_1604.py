# Generated by Django 3.1.7 on 2021-04-17 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0004_paciente_tratamento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='tratamento',
            field=models.BooleanField(verbose_name='Tratamento Concluido'),
        ),
    ]