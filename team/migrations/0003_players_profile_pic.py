# Generated by Django 3.0.4 on 2020-05-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_remove_players_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
