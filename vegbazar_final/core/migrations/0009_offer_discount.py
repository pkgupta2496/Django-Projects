# Generated by Django 3.0.6 on 2021-05-05 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_offer'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='discount',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
