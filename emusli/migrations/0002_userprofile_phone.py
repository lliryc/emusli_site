# Generated by Django 2.0.5 on 2018-06-11 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emusli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=256, null=True),
        ),
    ]