from django.db import models
from account.models import StudyLevel

# Create your models here.

class EDT(models.Model):
    image = models.ImageField(upload_to="edt_files")


"""
Nom cours 
Nom enseignant
"""
class Cours(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    teacher = models.CharField(max_length=100, null=False, blank=False)
    level  = models.CharField(choices=StudyLevel.choices)


class Filiere(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

