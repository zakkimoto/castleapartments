# Generated by Django 2.2.1 on 2019-05-15 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_property_buyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='buyer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='buyer.Buyer'),
        ),
    ]
