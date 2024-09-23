from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import get_user_model
from account.models import UserErayLearning
from courses.forms import EDTUploadForms


User = get_user_model()
# Create your views here.

# def edt_and_absence(request):
#     render(request, "account/login.html")


def edt_edit(request, user):
    user_req = UserErayLearning.objects.filter(username=user)
    if request.user.is_superuser:
        return render(request, "courses/edt_edit.html")
    return HttpResponse("<h2>OOOOOOOOOO</h2>")

def cours(request):
    return render(request, "courses/cours.html")

def notes(request):
    return render(request, "courses/notes.html")

def absence(request):
    return render(request, "courses/absence.html")

def dashboard(request):
    return render(request, "courses/dashboard.html")
