# Generated by Django 4.2.2 on 2023-06-24 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_alter_tipo_cantidad_personas_alter_tipo_duracion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='pago',
            field=models.CharField(choices=[('Co', 'Contado'), ('Cr', 'Credito')], max_length=2, null=True),
        ),
    ]
