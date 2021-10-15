import django_filters
from django import forms

from .models import Employee, Subdivision


class EmployeeFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    subdivision = django_filters.ModelMultipleChoiceFilter(queryset=Subdivision.objects.all())

    class Meta:
        model = Employee
        fields = '__all__'