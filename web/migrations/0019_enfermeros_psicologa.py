# Generated by Django 5.1.2 on 2024-10-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_doctores_alter_procedimientos_dependencia'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enfermeros', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Psicologa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('psicologa', models.CharField(max_length=80)),
            ],
        ),
    ]
