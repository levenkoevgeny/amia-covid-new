from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Subdivision(models.Model):
    subdivision_name = models.CharField(verbose_name="Подразделение", max_length=255)
    subdivision_short_name = models.CharField(
        verbose_name="Короткое название подразделения (только заглавные английские буквы)", max_length=255)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", blank=True, null=True)

    def __str__(self):
        return str(self.subdivision_name)

    class Meta:
        ordering = ('subdivision_name',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Employee(models.Model):
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, verbose_name="Подразделение", blank=True,
                                    null=True)
    covid_1_date = models.DateField(verbose_name="Дата первой прививки", blank=True, null=True)
    covid_2_date = models.DateField(verbose_name="Дата второй прививки", blank=True, null=True)
    is_willing = models.BooleanField(verbose_name="Желает пройти вакцинацию", default=False)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True)
    is_fired = models.BooleanField(verbose_name="Уволен", default=False)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'