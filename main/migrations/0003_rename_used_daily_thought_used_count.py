# Generated by Django 5.1.2 on 2024-11-07 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_daily_thought_author_daily_thought_used'),
    ]

    operations = [
        migrations.RenameField(
            model_name='daily_thought',
            old_name='used',
            new_name='used_count',
        ),
    ]
