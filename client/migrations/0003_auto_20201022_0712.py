# Generated by Django 3.0.10 on 2020-10-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20201021_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientsmasternew',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_address',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_cin',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_company',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_engagement',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_phone',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_position',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='clientsmasternew',
            name='client_teamname',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
