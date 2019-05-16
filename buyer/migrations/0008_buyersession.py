# Generated by Django 2.2.1 on 2019-05-15 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0007_auto_20190515_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuyerSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=200)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyer.Buyer')),
            ],
        ),
    ]