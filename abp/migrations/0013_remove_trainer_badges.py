# Generated by Django 2.1.4 on 2019-06-25 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0012_trainer_elite_tryouts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='badges',
        ),
    ]
