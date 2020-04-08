# Generated by Django 2.1.7 on 2020-04-04 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_ficha_fisica'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficha_fisica',
            name='percentual_gordura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
    ]
