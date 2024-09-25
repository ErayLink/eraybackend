from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserErayLearning, StudyLevel
from courses.models import Filiere, Note, Student

class InscriptionForm(UserCreationForm):
    filiere = forms.ModelChoiceField(queryset=Filiere.objects.all(), required=True, label="Filière")
    study_level = forms.ChoiceField(choices=StudyLevel.choices, required=True, label="Niveau d'étude")
    phone = forms.CharField(max_length=15, required=False, label="Téléphone")

    class Meta:
        model = UserErayLearning
        fields = ['username', 'password1', 'password2', 'filiere', 'study_level', 'phone']

    def __init__(self, *args, **kwargs):
        super(InscriptionForm, self).__init__(*args, **kwargs)
        # Personnaliser les widgets (facultatif)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control'})
        self.fields['filiere'].widget.attrs.update({'class': 'form-control'})
        self.fields['study_level'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone'].widget.attrs.update({'class': 'form-control'})



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

    # def __init__(self, *args, **kwargs):
    #     super(NoteForm, self).__init__(*args, **kwargs)
    #     # Limiter les choix d'étudiants à ceux qui sont effectivement enregistrés
    #     self.fields['student'].queryset = UserErayLearning.objects.filter(is_student=True)

