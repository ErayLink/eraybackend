from django.db import models
from django.contrib.auth.models import AbstractUser
from courses.models import Filiere

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
    # Lien avec une filière
    filiere = models.ForeignKey(Filiere, on_delete=models.SET_NULL, null=True, blank=True)
    # Niveau d'étude de l'étudiant
    study_level = models.CharField(
        max_length=10,
        choices=StudyLevel.choices,
        null=True,
        blank=True
    )
    
    # date_of_birth = models.DateField(null=True, blank=True)
    # address = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    matricule = models.CharField(max_length=50, null=False, blank=False, unique=True, editable=False)

    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        # Générer le matricule automatiquement pour les étudiants
        if self.is_student and not self.matricule:
            self.matricule = self.generate_matricule()
        super().save(*args, **kwargs)


    def generate_matricule(self):
    # Récupérer le dernier étudiant
        last_student = UserErayLearning.objects.filter(is_student=True).order_by('id').last()

        if last_student and last_student.matricule:
            last_number = int(last_student.matricule.split('-')[-1])
            new_number = last_number + 1
        else:
            new_number = 1

        # Ajoute la filière et le niveau d’étude au matricule
        filiere_code = self.filiere.name[:3].upper() if self.filiere else 'GEN'
        level_code = self.study_level if self.study_level else 'L1'
        return f"{level_code}-{filiere_code}-{new_number:05d}"
