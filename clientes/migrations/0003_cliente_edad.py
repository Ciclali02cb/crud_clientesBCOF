# Generated by Django 5.1.2 on 2024-11-23 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_cliente_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]