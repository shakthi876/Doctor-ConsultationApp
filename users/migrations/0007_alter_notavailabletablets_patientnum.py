# Generated by Django 4.0.2 on 2022-02-26 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_notavailabletablets_hospitalid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notavailabletablets',
            name='patientnum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.patientdetails'),
        ),
    ]
