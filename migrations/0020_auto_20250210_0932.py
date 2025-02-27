# Generated by Django 3.2.25 on 2025-02-10 06:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0019_auto_20250207_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffmovement',
            name='date_chosen',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 10, 6, 32, 41, 356771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='date_reported',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 10, 6, 32, 41, 356771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='last_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 10, 6, 32, 41, 356771, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='staffmovement',
            name='returned',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 10, 6, 32, 41, 356771, tzinfo=utc)),
        ),
    ]
