# Generated by Django 4.1.4 on 2022-12-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_remove_donarsinfo_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='donarsinfo',
            name='price',
            field=models.IntegerField(default=-1),
        ),
    ]