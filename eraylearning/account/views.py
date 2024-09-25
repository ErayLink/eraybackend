from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse
from .models import Filiere
from .forms import InscriptionForm


USER  = get_user_model()



# Create your views here.

def login_view(request):
    if request.method == "GET":
        user = request.user.is_authenticated
        if user:
            redirect("dashboard")
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Rediriger en fonction des rôles
                if user.is_student:
                    return redirect('dashboard')
                elif user.is_teacher:
                    return redirect('dashboard')
                else:
                    # Redirection par défaut si ni étudiant ni enseignant
                    return redirect('dashboard')  # Crée une vue ou une page par défaut
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe incorrect.")
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url="/", redirect_field_name="index")
def profile(request):
    return render(request, "account/profile.html")

def forgot_password(request):
    return HttpResponse('FORGOT')


# def inscription(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         filiere_name = request.POST.get("filiere")  # Récupère le nom de la filière
#         level = request.POST.get("level")

#         # Récupérer l'instance de Filiere correspondant au nom fourni
#         try:
#             filiere = Filiere.objects.get(name=filiere_name)
#         except Filiere.DoesNotExist:
#             messages.error(request, "La filière spécifiée n'existe pas.")
#             return redirect("inscription")

#         # Création de l'utilisateur
#         user = USER.objects.create_user(username=username, password=password, filiere=filiere, study_level=level)
        
#         # Connexion automatique après inscription
#         login(request, user=user)

#         return redirect("cours")

#     return render(request, "account/inscription.html")

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()  # Le modèle UserErayLearning est sauvegardé automatiquement
            login(request, user)
            return redirect('dashboard')  # Rediriger vers la page des cours après l'inscription
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = InscriptionForm()
    
    return render(request, 'account/inscription.html', {'form': form})


# def inscription(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         # firstname = request.POST.get("firstname")
#         # name = request.POST.get("name")
#         filiere = request.POST.get("filiere")
#         # mail = request.POST.get("mail")
#         level = request.POST.get("level")
#         # status = request.POST.get("status")
#         # Creation utilisateur
#         user = USER.objects.create_user(username=username, password=password, filiere=filiere, study_level=level)
#         login(request, user=user)

#         redirect("cours")

#     return render(request, "account/inscription.html")

