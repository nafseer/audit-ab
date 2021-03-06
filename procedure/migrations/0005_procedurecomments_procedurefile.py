# Generated by Django 3.0.10 on 2020-11-02 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0004_auto_20201102_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcedureComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('comments', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProcedureFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('notesfile', models.FileField(null=True, upload_to='')),
            ],
        ),
    ]
