# Generated by Django 2.2.7 on 2020-04-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='post',
            name='password',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
