# Generated by Django 5.0.6 on 2024-07-09 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('birth_date', models.DateField()),
                ('email', models.FloatField()),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, unique=True)),
                ('birth_date', models.DateField()),
                ('email', models.FloatField()),
                ('description', models.CharField(max_length=100, unique=True)),
                ('health_insurance_type', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'consulta',
            },
        ),
    ]
