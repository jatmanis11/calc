# Generated by Django 5.0.4 on 2024-05-13 12:35

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='news_title', unique=True),
        ),
    ]
