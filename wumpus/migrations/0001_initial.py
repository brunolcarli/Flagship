# Generated by Django 2.1.4 on 2021-03-08 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WumpusScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('performance', models.IntegerField()),
                ('rounds', models.IntegerField()),
                ('game_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
