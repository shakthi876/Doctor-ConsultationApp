# Generated by Django 4.0.2 on 2022-02-24 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_patientdetails_generalreason'),
    ]

    operations = [
        migrations.AddField(
            model_name='notavailabletablets',
            name='hospitalId',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
