# Generated by Django 2.1.4 on 2019-06-25 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0011_delete_elite'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='elite_tryouts',
            field=models.IntegerField(default=0),
        ),
    ]