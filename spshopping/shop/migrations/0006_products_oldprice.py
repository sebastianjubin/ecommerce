# Generated by Django 2.2 on 2023-01-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20230128_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='oldprice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
