# Generated by Django 2.1.4 on 2019-06-25 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0010_remove_trainer_elite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Elite',
        ),
    ]