# Generated by Django 5.1.1 on 2024-09-17 18:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_motivo_despliegue_despliegue_seguridad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accidentes_Transito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Atenciones_Paramedicas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Detalles_vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Lesionados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Rescate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_rescate', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Fallecidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_fallecimiento', models.CharField(max_length=50)),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=12)),
                ('edad', models.CharField(max_length=4)),
                ('sexo', models.CharField(max_length=10)),
                ('descripcion', models.CharField(max_length=50)),
                ('material_utilizado', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('id_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
        migrations.CreateModel(
            name='Falsa_Alarma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo_alarma', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
                ('material_utilizado', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('id_procedimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
        migrations.CreateModel(
            name='Rescate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_utilizado', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('id_procedimientos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
                ('tipo_rescate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipo_rescate')),
            ],
        ),
        migrations.CreateModel(
            name='Rescate_Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('especie', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
                ('id_rescate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.rescate')),
            ],
        ),
        migrations.CreateModel(
            name='Rescate_Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellidos', models.CharField(max_length=30)),
                ('cedula', models.CharField(max_length=10)),
                ('edad', models.CharField(max_length=3)),
                ('sexo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=30)),
                ('id_rescate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.rescate')),
            ],
        ),
        migrations.CreateModel(
            name='Servicios_Espaciales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_servicio', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=50)),
                ('material_utilizado', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=20)),
                ('id_procedimientos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.procedimientos')),
            ],
        ),
    ]
