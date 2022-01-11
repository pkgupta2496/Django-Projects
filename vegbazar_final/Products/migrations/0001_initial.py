# Generated by Django 3.0.6 on 2021-04-24 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.CharField(max_length=50)),
                ('product_img', models.ImageField(upload_to='myimage')),
                ('product_available_quantity', models.IntegerField()),
                ('is_product_veg', models.BooleanField()),
                ('is_product_fruit', models.BooleanField()),
                ('is_top_deal', models.BooleanField()),
            ],
        ),
    ]