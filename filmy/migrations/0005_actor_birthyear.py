# Generated by Django 5.0.4 on 2024-05-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmy', '0004_actor'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='birthyear',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]