# Generated by Django 2.2.15 on 2020-08-08 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0004_auto_20200808_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarship',
            name='school_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
