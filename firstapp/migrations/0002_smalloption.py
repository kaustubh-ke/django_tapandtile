# Generated by Django 3.0.6 on 2020-06-07 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SmallOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('detail', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='option')),
            ],
        ),
    ]
