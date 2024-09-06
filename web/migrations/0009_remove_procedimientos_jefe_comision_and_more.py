# Generated by Django 5.1.1 on 2024-09-06 19:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_rename_fecha_procedimientos_fecha_hora_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedimientos',
            name='jefe_comision',
        ),
        migrations.RemoveField(
            model_name='procedimientos',
            name='solicitante',
        ),
        migrations.AddField(
            model_name='procedimientos',
            name='id_solicitante',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.personal'),
            preserve_default=False,
        ),
    ]
