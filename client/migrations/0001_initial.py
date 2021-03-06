# Generated by Django 3.0.10 on 2020-10-21 21:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DesignationMasterNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_designation', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RolesMasterNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_role', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ClientsMasterNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_engagement', models.CharField(blank=True, max_length=150)),
                ('client_company', models.CharField(blank=True, max_length=150)),
                ('client_cin', models.CharField(blank=True, max_length=150)),
                ('client_address', models.CharField(blank=True, max_length=200)),
                ('client_doi', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('client_teamname', models.CharField(blank=True, max_length=200)),
                ('client_name', models.CharField(blank=True, max_length=150)),
                ('client_position', models.CharField(blank=True, max_length=150)),
                ('client_email', models.CharField(blank=True, max_length=150)),
                ('client_phone', models.CharField(blank=True, max_length=150)),
                ('client_designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sample3', to='client.DesignationMasterNew')),
                ('client_role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sample4', to='client.RolesMasterNew')),
            ],
        ),
    ]
