# Generated by Django 3.0.10 on 2020-10-17 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LeadsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leads_id', models.PositiveIntegerField(null=True)),
                ('leads_name', models.CharField(blank=True, max_length=50)),
                ('leads_description', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]