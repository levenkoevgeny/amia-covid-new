from django.shortcuts import render
from .models import Employee, VaccineCourse, VaccineKind, Subdivision
from .filters import EmployeeFilter, SubdivisionFilter
from django.shortcuts import get_object_or_404
from .forms import VaccineCourseForm, EmployeeDataForm, EmployeeFullDataForm
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404
from django.db import transaction
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required


def subdivision_get_employee_count_sum(subdivisions_list):
    count = 0
    for subdivision in subdivisions_list:
        count += subdivision.get_employee_count
    return count


def subdivision_get_covid_1_count_sum(subdivisions_list):
    count = 0
    for subdivision in subdivisions_list:
        count += subdivision.get_employee_count_with_first_vaccine
    return count


def subdivision_get_covid_2_count_sum(subdivisions_list):
    count = 0
    for subdivision in subdivisions_list:
        count += subdivision.get_employee_count_with_second_vaccine
    return count

# def get_willing_count_sum(subdivision_list):
#     count = 0
#     for subdivision in subdivision_list:
#         count += subdivision.get_willing_count
#     return count


def subdivision_get_covid_percent_sum_first(subdivisions_list):
    try:
        res = subdivision_get_covid_1_count_sum(subdivisions_list) / subdivision_get_employee_count_sum(subdivisions_list) * 100
    except ZeroDivisionError:
        res = 0.0
    return round(res, 2)


def subdivision_get_covid_percent_sum_second(subdivisions_list):
    try:
        res = subdivision_get_covid_2_count_sum(subdivisions_list) / subdivision_get_employee_count_sum(subdivisions_list) * 100
    except ZeroDivisionError:
        res = 0.0
    return round(res, 2)



#
#
# def get_employee_count_sum(employees_list):
#     count = 0
#     for employee in employees_list:
#         count += employee.get_employee_count
#     return count
#
#
# def get_employee_covid_1_count_sum(employees_list):
#     count = 0
#     for employee in employees_list:
#         count += employee.get_employee_count_with_first_vaccine
#     return count
#
#
# def get_employee_covid_2_count_sum(employees_list):
#     count = 0
#     for employee in employees_list:
#         count += employee.get_employee_count_with_second_vaccine
#     return count
#
#
# def get_employee_covid_percent_sum_first(employees_list):
#     try:
#         res = subdivision_get_covid_1_count_sum(employees_list) / subdivision_get_employee_count_sum(employees_list) * 100
#     except ZeroDivisionError:
#         res = 0.0
#     return round(res, 2)
#
#
# def get_employee_covid_percent_sum_second(subdivisions_list):
#     try:
#         res = subdivision_get_covid_2_count_sum(subdivisions_list) / subdivision_get_employee_count_sum(subdivisions_list) * 100
#     except ZeroDivisionError:
#         res = 0.0
#     return round(res, 2)

@login_required
def employee_list(request):
    path = str(request.get_full_path())
    request.session['next_path'] = path
    employees_list = Employee.objects.all()
    f = EmployeeFilter(request.GET, queryset=employees_list, request=request)
    condition = "all"
    if 'is_vaccinated' in request.GET:
        if request.GET['is_vaccinated'] == "all":
            result = f.qs
        else:
            condition = bool(request.GET['is_vaccinated'])
            result = [row for row in f.qs if row.get_is_vaccinated is condition]
    else:
        result = f.qs
    return render(request, 'covid/employee/employee_list.html',
                  {'employees_list': result,
                   'filter': f,
                   'condition': str(condition),
                   })


@login_required
def employee_input(request):
    if request.method == 'POST':
        form = EmployeeFullDataForm(request.POST)
        if form.is_valid():
            form.save()
            if 'next_path' in request.session:
                return HttpResponseRedirect(request.session.get('next_path'))
            else:
                return HttpResponseRedirect(reverse('covid:list'))
        else:
            return render(request, 'covid/employee/employee_input_form.html', {'form': form})
    else:
        form = EmployeeFullDataForm()
        return render(request, 'covid/employee/employee_input_form.html', {'form': form, })


@login_required
def employee_update(request, employee_id):
    if request.method == 'POST':
        obj = get_object_or_404(Employee, pk=employee_id)
        if request.user.is_superuser:
            form = EmployeeFullDataForm(request.POST, instance=obj)
        else:
            form = EmployeeDataForm(request.POST, instance=obj)
        if form.is_valid():
            employee_data = form.save()
            if not employee_data.has_contraindications:
                employee_data.contraindications_explain = ""
                employee_data.save()
            if 'next_path' in request.session:
                return HttpResponseRedirect(request.session.get('next_path'))
            else:
                return HttpResponseRedirect(reverse('covid:list'))
        else:
            return render(request, 'covid/employee/employee_update_form.html', {'form': form, 'employee': obj, })
    else:
        employee = get_object_or_404(Employee, pk=employee_id)
        if request.user.is_superuser:
            form = EmployeeFullDataForm(instance=employee)
            return render(request, 'covid/employee/employee_update_form_full.html',
                          {'form': form, 'employee': employee})
        else:
            form = EmployeeDataForm(instance=employee)
            return render(request, 'covid/employee/employee_update_form.html', {'form': form, 'employee': employee})


@login_required
def employee_info(request, employee_id):
    path = str(request.get_full_path())
    request.session['next_path'] = path
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'covid/employee/employee_info.html', {'employee': employee})


@login_required
def employee_vaccines(request, employee_id):
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
    return render(request, 'covid/vaccine/vaccine_add.html', {'employee_id': employee_id,
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
    return render(request, 'covid/vaccine/vaccine_update.html', {
        'vac_course': vac_course,
        'form': form
    })


@login_required
def employee_delete(request):
    return render(request, 'covid/employee/employee_delete_confirm.html')


@login_required
def subdivision_list(request):
    req_user = request.user
    if req_user.is_superuser:
        subdivisions_list = Subdivision.objects.all()
    else:
        subdivisions_list = Subdivision.objects.filter(owner=request.user)
    f = SubdivisionFilter(request.GET, queryset=subdivisions_list)
    return render(request, 'covid/subdivision/subdivision_list.html',
                  {
                      'subdivisions_list': f.qs,
                      'filter': f,
                      'employee_count_sum': subdivision_get_employee_count_sum(f.qs),
                      'employee_count_sum_first_vaccine': subdivision_get_covid_1_count_sum(f.qs),
                      'employee_count_sum_second_vaccine': subdivision_get_covid_2_count_sum(f.qs),
                      'employee_percent_first': subdivision_get_covid_percent_sum_first(f.qs),
                      'employee_percent_second': subdivision_get_covid_percent_sum_second(f.qs),
                  })
