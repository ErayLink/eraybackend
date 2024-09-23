from django.contrib import admin
from .models import Filiere, Note, Student, Cours, EDT

# Register your models here.


admin.site.register(Filiere)
admin.site.register(Note)
admin.site.register(Student)
admin.site.register(Cours)
admin.site.register(EDT)
