# Generated by Django 3.0.10 on 2020-10-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_id', models.PositiveIntegerField(null=True)),
                ('trail_account', models.CharField(blank=True, max_length=50)),
                ('trail_sheets', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
