# Generated by Django 3.1.3 on 2020-11-12 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='medstore/pics'),
        ),
    ]
