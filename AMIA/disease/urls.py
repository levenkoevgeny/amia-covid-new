from django.urls import path
from . import views


app_name = 'disease'

urlpatterns = [
    path('', views.index, name='index'),
    path('disease-list/', views.disease_list, name='disease-list'),
    # path('<subdivision_id>/update', views.subdivision_update, name='subdivision_update'),
    # path('subdivision/<subdivision_id>/employees_list', views.employees_list, name='employees'),
    # path('employee/<employee_id>/update', views.employee_update, name='employee_update'),
    # path('employee/add', views.employee_add, name='employee_add'),
    # path('employees-not-vaccinated', views.employee_list_not_vaccinated, name='employee_list_not_vaccinated'),
    # path('init', views.init, name='init'),
]