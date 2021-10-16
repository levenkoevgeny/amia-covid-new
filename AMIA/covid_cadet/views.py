from django.shortcuts import render


def subdivision_list(request):
    return render(request, 'covid_kadet/subdivisions/subdivision_list.html')


def course_list(request, subdivision_id):
    return render(request, 'covid_kadet/courses/course_list.html')


def employee_cadet_list(request, course_id):
    return render(request, 'covid_kadet/employee_cadet/employee_list.html')


def employee_cadet_input(request):
    return render(request, 'covid_kadet/employee_cadet/employee_input_form.html')


def employee_cadet_update(request, employee_cadet_id):
    return render(request, 'covid_kadet/employee_cadet/employee_update_form.html')


def employee_cadet_update_full(request, employee_cadet_id):
    return render(request, 'covid_kadet/employee_cadet/employee_update_form_full.html')
