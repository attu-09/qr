# Generated by Django 3.1.3 on 2020-12-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrApp', '0004_auto_20201224_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bjpdata',
            name='Date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
