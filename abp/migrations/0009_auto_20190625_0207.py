# Generated by Django 2.1.4 on 2019-06-25 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0008_auto_20190625_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='leader',
            name='nickname',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='name',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='nickname',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
