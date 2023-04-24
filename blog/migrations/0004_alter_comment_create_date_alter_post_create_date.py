# Generated by Django 4.1 on 2023-04-24 16:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_comment_create_date_alter_comment_post_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 24, 16, 57, 35, 426056, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="create_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 4, 24, 16, 57, 35, 425378, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]