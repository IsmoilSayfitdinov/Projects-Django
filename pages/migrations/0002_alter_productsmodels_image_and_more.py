# Generated by Django 5.0.6 on 2024-05-24 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsmodels',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='productsmodels',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
