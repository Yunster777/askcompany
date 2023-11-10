# Generated by Django 4.2.6 on 2023-11-07 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("instagram", "0005_post_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                limit_choices_to={"is_public": True},
                on_delete=django.db.models.deletion.CASCADE,
                to="instagram.post",
            ),
        ),
    ]
