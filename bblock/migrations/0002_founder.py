# Generated by Django 3.1.1 on 2020-10-04 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bblock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='founder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('founder_name', models.CharField(max_length=50)),
                ('des', models.CharField(max_length=300)),
                ('branch', models.CharField(default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='static')),
                ('facebbok_name', models.CharField(max_length=30)),
                ('home_town', models.CharField(max_length=30)),
            ],
        ),
    ]
