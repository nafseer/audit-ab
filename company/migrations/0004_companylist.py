# Generated by Django 3.0.10 on 2020-10-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0003_delete_companylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
