# Generated by Django 3.0.3 on 2020-10-07 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_auto_20191005_0359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='importado',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='ncm',
        ),
        migrations.RemoveField(
            model_name='produto',
            name='preco',
        ),
    ]
