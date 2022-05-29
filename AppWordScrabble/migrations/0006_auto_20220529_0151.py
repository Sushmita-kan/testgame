# Generated by Django 3.2.13 on 2022-05-29 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWordScrabble', '0005_auto_20220529_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedetails',
            name='PlayedBy',
            field=models.CharField(blank=True, default='No One', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='gamedetails',
            name='ScoreGained',
            field=models.IntegerField(blank=True, default=-3, null=True),
        ),
    ]
