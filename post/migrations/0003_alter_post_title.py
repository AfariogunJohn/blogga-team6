# Generated by Django 4.1.1 on 2022-10-23 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("post", "0002_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="title",
            field=models.CharField(max_length=500, unique=True),
        ),
    ]
