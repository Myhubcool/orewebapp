# Generated by Django 2.1.3 on 2019-02-10 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aio', '0002_all_auid'),
    ]

    operations = [
        migrations.AddField(
            model_name='all',
            name='ascolony',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='all',
            name='asdistrict',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='all',
            name='aspinno',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='all',
            name='asstate',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
