# Generated by Django 3.1.7 on 2021-03-19 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210319_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='users',
            field=models.ManyToManyField(related_name='channels', to='news.User'),
        ),
        migrations.DeleteModel(
            name='Userchannel',
        ),
    ]