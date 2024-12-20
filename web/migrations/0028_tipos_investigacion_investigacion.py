# Generated by Django 5.1.2 on 2024-10-24 17:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0027_remove_inspeccion_habitabilidad_id_inspeccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tipos_Investigacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_investigacion', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_procedimientos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
                ('id_tipo_investigacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipos_investigacion')),
            ],
        ),
    ]
