from django.forms import ModelForm
from .models import VaccineCourse
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class VaccineCourseForm(ModelForm):
    class Meta:
        model = VaccineCourse
        fields = ['vaccine_kind', 'date1', 'date2']
        widgets = {'date1': myDateInput,
                   'date2': myDateInput}
