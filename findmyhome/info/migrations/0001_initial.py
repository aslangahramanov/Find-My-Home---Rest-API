# Generated by Django 4.1.7 on 2023-03-13 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OnSaleHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=4)),
                ('square_price', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=50)),
                ('rooms', models.CharField(max_length=50)),
                ('title_deed', models.BooleanField(blank=True, default=True, null=True)),
                ('mortgage', models.BooleanField(blank=True, default=True, null=True)),
                ('repair', models.BooleanField(blank=True, default=True, null=True)),
                ('residential', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RentalHouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('currency', models.CharField(max_length=4)),
                ('category', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=50)),
                ('rooms', models.CharField(max_length=50)),
                ('repair', models.BooleanField(blank=True, default=True, null=True)),
                ('residential', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
