# Generated by Django 2.2 on 2023-02-01 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_products_oldprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='categ',
            name='img1',
            field=models.ImageField(default=1, upload_to='category'),
            preserve_default=False,
        ),
    ]
