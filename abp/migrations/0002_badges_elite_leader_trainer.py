# Generated by Django 2.1.4 on 2019-06-25 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal', models.BooleanField(default=False)),
                ('rock', models.BooleanField(default=False)),
                ('electric', models.BooleanField(default=False)),
                ('ghost', models.BooleanField(default=False)),
                ('ice', models.BooleanField(default=False)),
                ('poison', models.BooleanField(default=False)),
                ('water', models.BooleanField(default=False)),
                ('dark', models.BooleanField(default=False)),
                ('grass', models.BooleanField(default=False)),
                ('dragon', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Elite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bug', models.BooleanField(default=False)),
                ('steel', models.BooleanField(default=False)),
                ('fire', models.BooleanField(default=False)),
                ('fairy', models.BooleanField(default=False)),
                ('try_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nickname', models.CharField(max_length=150)),
                ('num_badges', models.IntegerField(default=0)),
                ('num_wins', models.IntegerField(default=0)),
                ('num_losses', models.IntegerField(default=0)),
                ('num_battles', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nickname', models.CharField(max_length=150)),
                ('num_badges', models.IntegerField(default=0)),
                ('num_wins', models.IntegerField(default=0)),
                ('num_losses', models.IntegerField(default=0)),
                ('num_battles', models.IntegerField(default=0)),
            ],
        ),
    ]