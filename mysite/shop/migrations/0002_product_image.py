# Generated by Django 4.2.9 on 2024-01-04 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to='product_images/'),
        ),
    ]
