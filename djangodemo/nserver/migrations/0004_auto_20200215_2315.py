# Generated by Django 3.0.3 on 2020-02-15 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nserver', '0003_auto_20200215_2315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='PublishDate',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
