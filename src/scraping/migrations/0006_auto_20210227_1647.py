# Generated by Django 3.1.6 on 2021-02-27 13:47

from django.db import migrations
import jsonfield.fields
import scraping.models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0005_auto_20210224_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='error',
            name='data',
            field=jsonfield.fields.JSONField(default=scraping.models.get_default_data_errors),
        ),
    ]
