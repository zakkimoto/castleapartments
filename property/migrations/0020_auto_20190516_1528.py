# Generated by Django 2.2.1 on 2019-05-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0019_auto_20190516_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='on_sale',
            field=models.BooleanField(default=True),
        ),
    ]
