# Generated by Django 3.1.3 on 2020-12-24 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrApp', '0002_auto_20201224_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bjpdata',
            name='Date',
            field=models.DateTimeField(),
        ),
    ]
