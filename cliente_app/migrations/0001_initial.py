# Generated by Django 5.1.3 on 2024-11-23 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_clien', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('celular', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=40)),
                ('fecha_nac', models.DateField()),
                ('email', models.CharField(max_length=60)),
            ],
        ),
    ]
