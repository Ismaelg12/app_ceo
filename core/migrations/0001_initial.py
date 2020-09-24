# Generated by Django 3.0.3 on 2020-09-22 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controle_usuarios', '0001_initial'),
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
            name='ListaEspera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('data_nascimento', models.DateField(blank=True, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('cpf', models.CharField(blank=True, max_length=14, null=True)),
                ('sus', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone Principal')),
                ('telefone_fixo', models.CharField(blank=True, max_length=20, verbose_name='Telefone Fixo')),
                ('observacao', models.TextField(blank=True, max_length=500)),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('profissional', models.ManyToManyField(to='controle_usuarios.Profissional')),
            ],
            options={
                'verbose_name': 'Lista de Espera',
                'verbose_name_plural': 'Listas de Espera',
            },
        ),
    ]
