# Generated by Django 5.0.1 on 2024-02-07 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_customuser_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
    ]