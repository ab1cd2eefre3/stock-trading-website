# Generated by Django 3.0.2 on 2021-03-01 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0006_auto_20210228_0211'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='closed',
            options={'verbose_name_plural': 'Closed'},
        ),
        migrations.AlterField(
            model_name='closed',
            name='stock_symbol',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='open',
            name='stock_symbol',
            field=models.CharField(max_length=30),
        ),
    ]
