# Generated by Django 2.2.1 on 2019-05-15 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_auto_20190515_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]