# Generated by Django 5.1.1 on 2024-09-17 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_feelings_moodentry_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodentry',
            name='price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]