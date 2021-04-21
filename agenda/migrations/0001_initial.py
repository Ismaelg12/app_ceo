# Generated by Django 3.1.7 on 2021-04-21 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('controle_usuarios', '0001_initial'),
        ('pacientes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(null=True)),
                ('hora', models.TimeField(null=True)),
                ('telefone', models.CharField(blank=True, max_length=15)),
                ('observacao', models.TextField(blank=True)),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('status', models.CharField(blank=True, choices=[('AG', 'Agendado'), ('AT', 'Atendido'), ('FN', 'Falta Não Justificada'), ('DM', 'Desmarcado')], default='AG', max_length=2)),
                ('atualizado_em', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacientes.paciente')),
                ('profissional', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='controle_usuarios.profissional')),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
            },
        ),
    ]
