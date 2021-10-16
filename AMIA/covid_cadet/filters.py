import django_filters
from django import forms

from .models import EmployeeCadet, Group


class EmployeeFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    group_fk = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())

    class Meta:
        model = EmployeeCadet
        fields = '__all__'