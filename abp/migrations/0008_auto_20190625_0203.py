# Generated by Django 2.1.4 on 2019-06-25 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0007_leader_battles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='badges',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abp.Badges'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='elite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='abp.Elite'),
        ),
    ]
