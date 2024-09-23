from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Exemple de niveaux d'étude possibles
class StudyLevel(models.TextChoices):
    L1 = 'L1', 'Licence 1'
    L2 = 'L2', 'Licence 2'
    L3 = 'L3', 'Licence 3'
    M1 = 'M1', 'Master 1'
    M2 = 'M2', 'Master 2'

class UserErayLearning(AbstractUser):
    is_student = models.BooleanField(default=True)
    is_teacher = models.BooleanField(default=False)
    
    # Niveau d'étude de l'étudiant
    study_level = models.CharField(
        max_length=10,
        choices=StudyLevel.choices,
        null=True,
        blank=True
    )
    
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    matricule = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # Générer le matricule automatiquement pour les étudiants
        if self.is_student and not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)


    def generate_matricule(self):
        # Récupérer le dernier utilisateur étudiant
        last_student = UserErayLearning.objects.filter(is_student=True).order_by('id').last()
        
        if last_student and last_student.matricule:
            # Extraire la partie numérique du matricule et l'incrémenter
            last_matricule = last_student.matricule
            try:
                last_number = int(last_matricule.split('-')[-1])  # Extrait la partie numérique
            except ValueError:
                last_number = 0  # Si le matricule n'a pas de partie numérique, on démarre à 0
            new_number = last_number + 1
        else:
            # Si c'est le premier étudiant
            new_number = 1

        # Générer le matricule sous le format souhaité, par exemple "STU-0001"
        return f"student-{new_number:05d}-{self.username}"