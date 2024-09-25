from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .forms import FiliereForm, NoteForm
from .models import Filiere

User = get_user_model()
# Create your views here.

def edt(request):
   return render(request, "courses/edt_and_absence.html")

# @login_required
# def edt_edit(request, user):
#     user_req = UserErayLearning.objects.filter(username=user)
#     if request.user.is_superuser:
#         return render(request, "courses/edt_edit.html")
#     return HttpResponse("<h2>OOOOOOOOOO</h2>")


@login_required(login_url="/", redirect_field_name="index")
def cours(request):
    return render(request, "courses/cours.html")

@login_required(login_url="/", redirect_field_name="index")
def notes(request):
    return render(request, "courses/notes.html")


@login_required(login_url="/", redirect_field_name="index")
def absence(request):
    return render(request, "courses/absence.html")


@login_required(login_url="/", redirect_field_name="index")
def dashboard(request):
    filiere = Filiere.objects.filter()
    context = {
        "filiere": filiere
    }
    return render(request, "courses/dashboard.html", context=context)

# from .models import Filiere, Note

def gestion_filiere_et_note(request):
    if request.method == 'POST':
        if 'create_filiere' in request.POST:
            filiere_form = FiliereForm(request.POST)
            if filiere_form.is_valid():
                filiere_form.save()
                return redirect('gestion_filiere_et_note')  # Redirige vers la même page
        elif 'create_note' in request.POST:
            note_form = NoteForm(request.POST)
            if note_form.is_valid():
                note_form.save()
                return redirect('gestion_filiere_et_note')  # Redirige vers la même page
    else:
        filiere_form = FiliereForm()
        note_form = NoteForm()

    return render(request, 'courses/gestion_filiere_et_note.html', {
        'filiere_form': filiere_form,
        'note_form': note_form,
    })
