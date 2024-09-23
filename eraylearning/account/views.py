from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def login_view(request):
    return render(request, "account/login.html") #Miandry login PAGES


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def profile(request):
    return render(request, "account/profile.html")

def forgot_password(request):
    return HttpResponse('FORGOT')
