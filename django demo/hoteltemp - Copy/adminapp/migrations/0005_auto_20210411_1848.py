# Generated by Django 3.1.6 on 2021-04-11 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('adminapp', '0004_rooms_r_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='r_image',
            field=models.ImageField(upload_to='images'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('persons', models.IntegerField()),
                ('status', models.IntegerField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.login')),
            ],
        ),
    ]
