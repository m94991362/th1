# Generated by Django 2.2.3 on 2019-07-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='amount',
            field=models.BigIntegerField(default=0),
        ),
    ]
