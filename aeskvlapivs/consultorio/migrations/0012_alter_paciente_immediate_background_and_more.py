# Generated by Django 4.0.5 on 2022-07-05 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultorio', '0011_alter_paciente_immediate_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='immediate_background',
            field=models.TextField(verbose_name='Padecimiento, Razón de Abordaje o Situación Actual'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tension_diastolica',
            field=models.PositiveSmallIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='tension_sistolica',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
