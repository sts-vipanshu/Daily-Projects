from django import forms

from .models import StudentData


class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentData
        fields = "__all__"
