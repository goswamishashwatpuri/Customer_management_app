# Generated by Django 3.1 on 2020-09-21 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200921_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default=' ', null=True, upload_to=''),
        ),
    ]