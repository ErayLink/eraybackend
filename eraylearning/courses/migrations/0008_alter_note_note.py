# Generated by Django 5.1.1 on 2024-09-23 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_edt_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
