# Generated by Django 2.2.7 on 2019-11-26 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='user',
            field=models.ManyToManyField(blank=True, to='home.User'),
        ),
    ]