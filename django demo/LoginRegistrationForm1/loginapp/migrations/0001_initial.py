# Generated by Django 3.1.1 on 2020-09-14 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=10)),
                ('role', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('profilepic', models.ImageField(upload_to='images')),
                ('courseid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('loginid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginapp.login')),
            ],
        ),
    ]
