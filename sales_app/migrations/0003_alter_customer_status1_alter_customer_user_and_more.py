# Generated by Django 5.0.3 on 2024-04-15 14:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales_app', '0002_rename_status1_seller_status2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='status1',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='seller',
            name='status2',
            field=models.BooleanField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='seller',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
