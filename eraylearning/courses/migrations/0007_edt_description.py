# Generated by Django 5.1.1 on 2024-09-23 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_cours_level_alter_student_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='edt',
            name='description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
