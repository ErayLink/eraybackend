"""eraylearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from courses import views
from account.views import login_view, logout_user, profile, inscription

urlpatterns = [
    path('gestion/', views.gestion_filiere_et_note, name='gestion_filiere_et_note'),
    path("", login_view, name="index"), #Return LOGIN PAGES
    path("dashboard/", views.dashboard, name="dashboard"),
    path("cours/", views.cours, name="cours"),
    path("notes/", views.notes, name="notes"),
    path("absence/", views.absence, name="absence"),
    path("edt/", views.edt, name="edt"),
    path('admin/', admin.site.urls),
    path("logout/", logout_user , name="logout"),
    path("profile/", profile , name="profile"),
    path("inscription/", inscription , name="inscription"),

]
