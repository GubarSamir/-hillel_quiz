# Generated by Django 3.2.6 on 2021-08-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210816_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='raiting',
            field=models.IntegerField(default=0),
        ),
    ]