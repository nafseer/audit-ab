# Generated by Django 3.0.10 on 2020-10-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_id', models.PositiveIntegerField(null=True)),
                ('role_name', models.CharField(blank=True, max_length=50)),
                ('role_description', models.CharField(blank=True, max_length=50)),
                ('module_one', models.CharField(blank=True, max_length=50)),
                ('module_two', models.CharField(blank=True, max_length=1)),
                ('module_three', models.CharField(blank=True, max_length=15)),
                ('module_four', models.CharField(blank=True, max_length=15)),
                ('module_five', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
