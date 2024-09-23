from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from account.models import UserErayLearning
from courses.forms import EDTUploadForms
from django.contrib.auth.decorators import login_required

User = get_user_model()
# Create your views here.

# def edt_and_absence(request):
#     render(request, "account/login.html")

@login_required
def edt_edit(request, user):
    user_req = UserErayLearning.objects.filter(username=user)
    if request.user.is_superuser:
        return render(request, "courses/edt_edit.html")
    return HttpResponse("<h2>OOOOOOOOOO</h2>")


@login_required
def cours(request):
    return render(request, "courses/cours.html")

@login_required
def notes(request):
    return render(request, "courses/notes.html")


@login_required
def absence(request):
    return render(request, "courses/absence.html")


@login_required
def dashboard(request):
    return render(request, "courses/dashboard.html")
