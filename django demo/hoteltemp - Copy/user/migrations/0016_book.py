# Generated by Django 3.1.6 on 2021-04-12 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_delete_book'),
        ('user', '0015_delete_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.CharField(max_length=10)),
                ('check_out', models.CharField(max_length=10)),
                ('persons', models.IntegerField()),
                ('status', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.login')),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.rooms')),
            ],
        ),
    ]
