# Generated by Django 3.0.10 on 2020-10-30 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('procedure', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceduremaster',
            name='notesfile',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
