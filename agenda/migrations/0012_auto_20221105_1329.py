# Generated by Django 3.0.3 on 2022-11-05 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20221102_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odontograma',
            name='descricao',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
