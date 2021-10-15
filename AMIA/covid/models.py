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
    position = models.CharField(verbose_name="Должность", max_length=255)

    def __str__(self):
        return self.position

    class Meta:
        ordering = ('position',)
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'


class Rank(models.Model):
    rank = models.CharField(verbose_name="Фамилия", max_length=50)

    def __str__(self):
        return self.rank

    class Meta:
        ordering = ('rank',)
        verbose_name = 'Звание'
        verbose_name_plural = 'Звания'


class Employee(models.Model):
    SEX = [
        (1, 'Мужской'),
        (2, 'Женский'),
    ]
    last_name = models.CharField(verbose_name="Фамилия", max_length=30)
    first_name = models.CharField(verbose_name="Имя", max_length=30, blank=True, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=30, blank=True, null=True)
    subdivision = models.ForeignKey(Subdivision, on_delete=models.SET_NULL, verbose_name="Подразделение", blank=True,
                                    null=True)
    sex = models.IntegerField(choices=SEX, verbose_name="Пол", blank=True, null=True)
    rank = models.ForeignKey(Rank, on_delete=models.CASCADE, verbose_name="Звание", blank=True, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, verbose_name="Должность", blank=True, null=True)
    phone_number = models.CharField(verbose_name="Номер телефона", max_length=30, blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True)

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


class VaccineCourse(models.Model):
    course_name = models.CharField(max_length=255, verbose_name="Название курса")
    vaccine_kind = models.ForeignKey(VaccineKind, on_delete=models.CASCADE, verbose_name="Вид вакцины")
    date1 = models.DateField(verbose_name="Дата проведения первой вакцинации", blank=True, null=True)
    date2 = models.DateField(verbose_name="Дата проведения второй вакцинации", blank=True, null=True)
    employees = models.ManyToManyField(Employee, through='Vaccination')

    def __str__(self):
        return self.vaccine_kind.kind

    class Meta:
        ordering = ('vaccine_kind',)
        verbose_name = 'Курс вакцинации'
        verbose_name_plural = 'Курсы вакцинации'


class Vaccination(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
    vaccine_course = models.ForeignKey(VaccineCourse, on_delete=models.CASCADE, verbose_name="Курс вакцинации")
    last_modified = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.employee.last_name

    class Meta:
        ordering = ('employee',)
        verbose_name = 'Вакцинация'
        verbose_name_plural = 'Вакцинации'

# class Vaccination(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name="Сотрудник")
#     vaccine_course = models.ForeignKey(VaccineCourse, on_delete=models.SET_NULL, verbose_name="Курс вакцинации",
#                                        null=True, blank=True)

    # vaccine_kind = models.ForeignKey(VaccineKind, on_delete=models.CASCADE, verbose_name="Вид вакцины")
    # date = models.DateField(verbose_name="Дата проведения вакцинации")

    # def __str__(self):
    #     return self.employee.last_name
    #
    # class Meta:
    #     ordering = ('employee',)
    #     verbose_name = 'Вакцинация'
    #     verbose_name_plural = 'Вакцинации'
