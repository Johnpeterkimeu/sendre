# Generated by Django 3.2.25 on 2025-02-07 10:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_auto_20250207_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffmovement',
            name='Other',
        ),
        migrations.RemoveField(
            model_name='staffmovement',
            name='Others',
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='date_chosen',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 10, 10, 35, 608015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='date_reported',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 10, 10, 35, 608015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 10, 10, 35, 608015, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='returned',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 7, 10, 10, 35, 608015, tzinfo=utc)),
        ),
    ]
