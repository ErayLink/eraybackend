from django.forms import ModelForm
from courses.models import EDT
from django import forms
from .models import Filiere, Note

class EDTUploadForms(ModelForm):
    class Meta:
        model = EDT
        fields = "__all__"




class FiliereForm(forms.ModelForm):
    class Meta:
        model = Filiere
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la filière'}),
        }

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['student', 'cours', 'note']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-control'}),
            'cours': forms.Select(attrs={'class': 'form-control'}),
            'note': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Note'}),
        }
