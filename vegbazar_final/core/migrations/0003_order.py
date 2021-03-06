# Generated by Django 3.0.6 on 2021-04-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_imageslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_img', models.ImageField(upload_to='OrderImage')),
                ('product_id', models.CharField(max_length=2)),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=10)),
                ('quantity', models.IntegerField()),
                ('total_price', models.CharField(max_length=10)),
                ('user_name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('mobile', models.CharField(max_length=10)),
            ],
        ),
    ]
