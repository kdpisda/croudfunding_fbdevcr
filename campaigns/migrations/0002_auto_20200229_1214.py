# Generated by Django 3.0.3 on 2020-02-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='end_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='start_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
