# Generated by Django 5.0.3 on 2024-05-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_mobileproduct_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobileproduct',
            name='price',
            field=models.IntegerField(),
        ),
    ]
