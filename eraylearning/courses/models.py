from django.db import models
from django.conf import settings

# Exemple de niveaux d'étude possibles
class StudyLevel(models.TextChoices):
    L1 = 'L1', 'Licence 1'
    L2 = 'L2', 'Licence 2'
    L3 = 'L3', 'Licence 3'
    M1 = 'M1', 'Master 1'
    M2 = 'M2', 'Master 2'

# Modèle pour les emplois du temps (EDT)
class EDT(models.Model):
    image = models.ImageField(upload_to="edt_files")
    description = models.TextField(max_length=200, null=True, blank=True, editable=True)
    
    def __str__(self):
        return f"| Emploi du temps {self.id} | {self.description} |"


# Modèle pour les cours
class Cours(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    teacher = models.CharField(max_length=100, null=False, blank=False)
    level = models.CharField(max_length=100, choices=StudyLevel.choices)


    def __str__(self):
        return f"{self.name} ({self.teacher})"

# Modèle pour les filières (par exemple, "Informatique", "Gestion", etc.)
class Filiere(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.name

# Modèle pour les étudiants (lié à un utilisateur)
class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    level = models.CharField(max_length=100, choices=StudyLevel.choices)  # Par exemple, L1, L2, M1, etc.
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)  # L'étudiant est lié à une filière

    def __str__(self):
        return f"{self.user.username}  |  {self.user.matricule}"
    
    

# Modèle pour les notes
class Note(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)  # Un étudiant
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE)  # Un cours
    note = models.DecimalField(max_digits=5, decimal_places=2)  # Note sur 100 par exemple
    date_assigned = models.DateTimeField(auto_now_add=True)  # Date d'attribution de la note

    class Meta:
        unique_together = ('student', 'cours')  # Un étudiant ne peut avoir qu'une seule note par cours

    def __str__(self):
        return f"Note: {self.note} - {self.student.user.username} - {self.cours.name}"


