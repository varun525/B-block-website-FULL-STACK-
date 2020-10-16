# Generated by Django 3.1.1 on 2020-10-09 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bblock', '0002_founder'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('contact_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('college', models.CharField(max_length=400)),
                ('town', models.CharField(default='', max_length=50)),
                ('mail', models.CharField(default='', max_length=50)),
                ('number', models.IntegerField(default=0)),
                ('text', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
