# Generated by Django 5.1.5 on 2025-02-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('glassblog', '0002_blogpost_topic'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
