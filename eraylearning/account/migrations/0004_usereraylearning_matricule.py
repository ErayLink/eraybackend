# Generated by Django 5.1.1 on 2024-09-20 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_usereraylearning_study_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='usereraylearning',
            name='matricule',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
    ]
