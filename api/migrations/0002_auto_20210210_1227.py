# Generated by Django 3.0.8 on 2021-02-10 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='image_url',
            field=models.CharField(max_length=500),
        ),
    ]
