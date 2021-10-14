from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Subdivision(models.Model):
    subdivision_name = models.CharField(verbose_name="Подразделение", max_length=255)
    subdivision_short_name = models.CharField(
        verbose_name="Короткое название подразделения (только заглавные английские буквы)", max_length=255)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name="Кто может вносить изменения", blank=True,
                              null=True)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", blank=True, null=True)

    def __str__(self):
        return str(self.subdivision_name)

    class Meta:
        ordering = ('subdivision_name',)
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class Position(models.Model):
    position = models.CharField(verbose_name="Фамилия", max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ('position',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Employee(models.Model):
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    first_name = models.CharField(verbose_name="Имя", max_length=30, blank=True, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30, blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, verbose_name="Подразделение", blank=True,
                                    null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, verbose_name="Должность", blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True)
    # vaccinations = models.ManyToManyField(Vaccination, through=Vaccination)

    def __str__(self):
        return self.last_name

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


class VaccineKind(models.Model):
    kind = models.CharField(max_length=30, verbose_name="Вид вакцины")

    def __str__(self):
        return self.kind

    class Meta:
        ordering = ('kind',)
        verbose_name = 'Вид вакцины'
        verbose_name_plural = 'Виды вакцины'


class Vaccination(models.Model):
    VACCINE_ORDER = [
        (1, 'Первая'),
        (2, 'Вторая'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    vaccine_kind = models.ForeignKey(VaccineKind, on_delete=models.CASCADE, verbose_name="Вид вакцины")
    date = models.DateField(verbose_name="Дата проведения вакцинации")
    order = models.IntegerField(choices=VACCINE_ORDER, verbose_name="Очередность вакцины")

    def __str__(self):
        return self.employee.last_name + ' ' + str(self.order) + ' ' + self.vaccine_kind.kind + ' ' + str(self.date)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Вакцинация'
        verbose_name_plural = 'Вакцинации'





