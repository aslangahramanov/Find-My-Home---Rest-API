# Generated by Django 4.1.7 on 2023-03-18 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_homeads_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeads',
            name='buy_or_rent',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]