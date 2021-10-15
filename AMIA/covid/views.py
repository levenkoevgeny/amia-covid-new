from django.shortcuts import render
from .models import Employee, VaccineCourse, VaccineKind
from .filters import EmployeeFilter
from django.shortcuts import get_object_or_404
from .forms import VaccineCourseForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse


def employee_list(request):
    path = str(request.get_full_path())
    request.session['next_path'] = path
    employees_list = Employee.objects.all()
    f = EmployeeFilter(request.GET, queryset=employees_list)
    return render(request, 'covid/employee_list.html',
                  {'employees_list': f.qs,
                   'filter': f}
                  )


def employee_input(request):
    return render(request, 'covid/employee_input_form.html')


def employee_update(request, employee_id):
    return render(request, 'covid/employee_update_form.html')


def employee_info(request):
    return render(request, 'covid/employee_info.html')


def employee_vaccines(request, employee_id):
    path = str(request.get_full_path())
    request.session['next_path'] = path
    employee = get_object_or_404(Employee, pk=employee_id)
    vaccine_kind_list = VaccineKind.objects.all()
    return render(request, 'covid/employee_vaccines.html',
                  {
                      'employee': employee,
                      'vaccine_kind_list': vaccine_kind_list,
                  })


def employee_vaccines_add_form(request, employee_id):
    if request.method == 'POST':
        form = VaccineCourseForm(request.POST)
        if form.is_valid():
            vac_course = form.save(commit=False)
            vac_course.employee = get_object_or_404(Employee, pk=employee_id)
            if vac_course.vaccine_kind.is_one_component:
                if vac_course.date1:
                    vac_course.date2 = vac_course.date1
            vac_course.save()
            return JsonResponse({'': ''}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)
    else:
        form = VaccineCourseForm()
    return render(request, 'covid/vaccine_add.html', {'employee_id': employee_id,
                                                      'form': form
                                                      })


def employee_vaccines_update_form(request, vaccine_course_id):
    if request.method == 'POST':
        obj = get_object_or_404(VaccineCourse, pk=vaccine_course_id)
        form = VaccineCourseForm(request.POST, instance=obj)
        if form.is_valid():
            vac_course = form.save(commit=False)
            if vac_course.vaccine_kind.is_one_component:
                if vac_course.date1:
                    vac_course.date2 = vac_course.date1
            vac_course.save()
            return JsonResponse({'': ''}, safe=False)
        else:
            error_message = "Заполните правильно форму!"
            return JsonResponse({'error': error_message}, safe=False)
    else:
        vac_course = get_object_or_404(VaccineCourse, pk=vaccine_course_id)
        form = VaccineCourseForm(instance=vac_course)
    return render(request, 'covid/vaccine_update.html', {
        'vac_course': vac_course,
        'form': form
    })


def employee_delete(request):
    return render(request, 'covid/employee_delete_confirm.html')
