# Generated by Django 3.2 on 2022-07-15 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user_profile',
            new_name='user',
        ),
    ]
