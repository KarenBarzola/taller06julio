# Generated by Django 4.2.2 on 2023-07-08 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0005_adicional'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notific',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celular', models.IntegerField()),
                ('datos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eventos.cliente')),
            ],
        ),
    ]
