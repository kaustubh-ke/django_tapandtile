# Generated by Django 3.0.6 on 2020-06-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_topproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='topproduct',
            name='offerprice',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='topproduct',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
