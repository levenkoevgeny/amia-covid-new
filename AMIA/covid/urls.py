from django.urls import path
from . import views


app_name = 'covid'

urlpatterns = [
    path('', views.employee_list, name='list'),
    path('add', views.employee_input, name='employee-add'),
    path('<employee_id>/update', views.employee_update, name='employee-update'),
    path('<employee_id>/vaccines', views.employee_vaccines, name='employee-vaccines'),
    path('<employee_id>/vaccines-add', views.employee_vaccines_add_form, name='employee-vaccines-add'),
    path('<employee_id>/<vaccine_course_id>/vaccines-update', views.employee_vaccines_update_form, name='employee-vaccines-update'),

    # path('', views.index, name='index'),
    # path('<subdivision_id>/update', views.subdivision_update, name='subdivision_update'),
    # path('subdivision/<subdivision_id>/employees_list', views.employees_list, name='employees'),
    # path('employee/<employee_id>/update', views.employee_update, name='employee_update'),
    # path('employee/add', views.employee_add, name='employee_add'),
    # path('employees-not-vaccinated', views.employee_list_not_vaccinated, name='employee_list_not_vaccinated'),
    # path('init', views.init, name='init'),
]