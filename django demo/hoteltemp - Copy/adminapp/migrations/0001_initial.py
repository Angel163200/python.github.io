# Generated by Django 3.1.6 on 2021-04-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('floor_no', models.IntegerField()),
                ('type', models.CharField(max_length=30)),
                ('size', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('view', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
            ],
        ),
    ]