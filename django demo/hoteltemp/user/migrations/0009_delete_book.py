# Generated by Django 3.1.6 on 2021-04-12 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_book'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]