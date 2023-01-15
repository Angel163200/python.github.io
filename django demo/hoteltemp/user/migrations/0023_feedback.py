# Generated by Django 3.1.6 on 2021-04-15 05:54

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_delete_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.TextField(max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.login')),
            ],
        ),
    ]