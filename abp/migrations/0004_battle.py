# Generated by Django 2.1.4 on 2019-06-25 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('abp', '0003_auto_20190625_0120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=100)),
                ('fight_date', models.DateField(auto_now_add=True)),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abp.Leader')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='abp.Trainer')),
            ],
        ),
    ]
