# Generated by Django 2.2.1 on 2019-05-13 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetname', models.CharField(max_length=225)),
                ('description', models.CharField(blank=True, max_length=999)),
                ('address', models.CharField(max_length=225)),
                ('postal_code', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=225)),
                ('country', models.CharField(max_length=200)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('size', models.FloatField()),
                ('price', models.FloatField()),
                ('on_sale', models.BooleanField()),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='PropertyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=999)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.Property')),
            ],
        ),
        migrations.AddField(
            model_name='property',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='property.PropertyType'),
        ),
    ]
