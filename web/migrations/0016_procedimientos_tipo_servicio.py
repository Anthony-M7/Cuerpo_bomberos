# Generated by Django 5.1.2 on 2024-10-21 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_procedimientos_efectivos_enviados_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='procedimientos',
            name='tipo_servicio',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
