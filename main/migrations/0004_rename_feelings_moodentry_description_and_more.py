# Generated by Django 5.1.1 on 2024-09-17 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_moodentry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moodentry',
            old_name='feelings',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='moodentry',
            old_name='mood',
            new_name='item',
        ),
    ]
