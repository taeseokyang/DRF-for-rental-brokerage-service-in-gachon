# Generated by Django 4.2.4 on 2023-08-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("comments", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment", name="postid", field=models.IntegerField(default=1),
        ),
    ]
