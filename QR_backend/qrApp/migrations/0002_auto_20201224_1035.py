# Generated by Django 3.1.3 on 2020-12-24 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bjpdata',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
