# Generated by Django 4.2.4 on 2023-08-18 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_rename_user_post_author"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0005_rename_user_comment_writer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post",
                to="posts.post",
            ),
        ),
        migrations.AlterField(
            model_name="comment",
            name="writer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="writer",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
