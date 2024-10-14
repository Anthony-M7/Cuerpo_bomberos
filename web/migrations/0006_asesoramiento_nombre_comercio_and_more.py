# Generated by Django 5.1.1 on 2024-10-10 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_reinspeccion_prevencion_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='asesoramiento',
            name='nombre_comercio',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asesoramiento',
            name='rif_comercio',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asesoramiento',
            name='sexo',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='asesoramiento',
            name='nombres',
            field=models.CharField(max_length=50),
        ),
    ]