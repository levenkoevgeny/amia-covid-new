import django_filters
from django import forms

from .models import EmployeeCadet, SubdivisionCadet, Group


class EmployeeCadetFilter(django_filters.FilterSet):
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    group_fk = django_filters.ModelMultipleChoiceFilter(queryset=Group.objects.all())

    class Meta:
        model = EmployeeCadet
        fields = '__all__'


class SubdivisionCadetFilter(django_filters.FilterSet):
    subdivisions_choices = set()

    for sub in SubdivisionCadet.objects.all():
        subdivisions_choices.add((sub.id, sub.subdivision_name))

    id = django_filters.MultipleChoiceFilter(choices=subdivisions_choices)

    class Meta:
        model = SubdivisionCadet
        fields = '__all__'
