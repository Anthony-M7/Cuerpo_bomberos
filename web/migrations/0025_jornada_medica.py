# Generated by Django 5.1.2 on 2024-10-24 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0024_alter_procedimientos_id_parroquia_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jornada_Medica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_jornada', models.CharField(max_length=100)),
                ('cant_personas_aten', models.CharField(max_length=4)),
                ('descripcion', models.CharField(max_length=100)),
                ('material_utilizado', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('id_procedimientos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
    ]
