from django.shortcuts import render
from .models import Employee, VaccineCourse
from .filters import EmployeeFilter
from django.shortcuts import get_object_or_404


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
    employee = get_object_or_404(Employee, pk=employee_id)
    vaccine_course_list = VaccineCourse.objects.all()
    return render(request, 'covid/employee_vaccines.html',
                  {
                      'employee': employee,
                      'vaccine_course_list': vaccine_course_list,
                  })


def employee_vaccines_add_form(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'covid/vaccine_add.html', {'employee': employee})


def employee_delete(request):
    return render(request, 'covid/employee_delete_confirm.html')
