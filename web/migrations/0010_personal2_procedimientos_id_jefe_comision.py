# Generated by Django 5.1.1 on 2024-09-06 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_remove_procedimientos_jefe_comision_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Personal2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('jerarquia', models.CharField(max_length=50)),
                ('cargo', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='procedimientos',
            name='id_jefe_comision',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='web.personal2'),
            preserve_default=False,
        ),
    ]
