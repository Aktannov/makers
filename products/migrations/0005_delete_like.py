# Generated by Django 4.0 on 2021-12-24 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_like_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]