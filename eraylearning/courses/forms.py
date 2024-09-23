from django.forms import ModelForm
from courses.models import EDT


class EDTUploadForms(ModelForm):
    class Meta:
        model = EDT
        fields = "__all__"