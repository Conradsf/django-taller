# Generated by Django 3.2.6 on 2021-08-13 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='clients',
            name='phone',
            field=models.CharField(max_length=9),
        ),
    ]
