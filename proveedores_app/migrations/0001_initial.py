# Generated by Django 5.1.3 on 2024-11-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('id_prod', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('ubicacion', models.CharField(max_length=30)),
                ('telefono', models.CharField(max_length=20)),
                ('hora', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
