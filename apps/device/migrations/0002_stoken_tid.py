# Generated by Django 2.1.4 on 2018-12-31 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stoken',
            name='tid',
            field=models.CharField(default=99, max_length=2),
            preserve_default=False,
        ),
    ]