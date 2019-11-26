# Generated by Django 2.2.7 on 2019-11-26 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191125_2015'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ingredients',
        ),
        migrations.AlterField(
            model_name='user',
            name='emergency_contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='home.EmergencyContact'),
        ),
        migrations.CreateModel(
            name='UserAllergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Ingredient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.User')),
            ],
        ),
    ]
