# Generated by Django 2.1.4 on 2019-06-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0015_auto_20190625_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='badges',
            field=models.ManyToManyField(null=True, to='abp.Badges'),
        ),
    ]