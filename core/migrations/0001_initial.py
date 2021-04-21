# Generated by Django 3.1.7 on 2021-04-21 15:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controle_usuarios', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_menu', models.ImageField(upload_to='media')),
                ('clinica', models.CharField(blank=True, max_length=50)),
                ('sobre_nos', models.TextField(blank=True, max_length=600)),
            ],
            options={
                'verbose_name': 'Clinica ',
                'verbose_name_plural': 'Clinica',
            },
        ),
        migrations.CreateModel(
            name='Especialidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
            },
        ),
        migrations.CreateModel(
            name='ListaEspera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.TextField(blank=True, max_length=500)),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('criado_em', models.DateField(default=datetime.datetime(2021, 4, 21, 15, 14, 23, 929450, tzinfo=utc), verbose_name='Criado em')),
                ('urgente', models.CharField(blank=True, choices=[('U', 'Urgente'), ('R', 'Não urgente')], max_length=1, verbose_name='Urgente')),
                ('especialidade', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.especialidade')),
                ('nome', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pacientes.paciente')),
                ('profissional', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='controle_usuarios.profissional')),
            ],
            options={
                'verbose_name': 'Lista de Espera',
                'verbose_name_plural': 'Listas de Espera',
            },
        ),
    ]
