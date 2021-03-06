from django.db import models


# факультет

class SubdivisionCadet(models.Model):
    subdivision_name = models.CharField(verbose_name="Подразделение", max_length=255)
    subdivision_short_name = models.CharField(
        verbose_name="Короткое название подразделения (только заглавные английские буквы)", max_length=255)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", blank=True, null=True)

    def __str__(self):
        return str(self.subdivision_name)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Факультет'
        verbose_name_plural = '1. Факультеты'


class Course(models.Model):
    course_name = models.CharField(verbose_name="Курс", max_length=255)
    faculty = models.ForeignKey(SubdivisionCadet, verbose_name="Факультет", on_delete=models.SET_NULL, blank=True,
                                null=True)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True,
                                         blank=True, null=True)

    class Meta:
        ordering = ('course_name',)
        verbose_name = 'Курс'
        verbose_name_plural = '2. Курсы'


class Group(models.Model):
    group_name = models.CharField(verbose_name="Группа", max_length=255)
    course = models.ForeignKey(Course, verbose_name="Курс", on_delete=models.SET_NULL, blank=True,
                               null=True)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True,
                                         blank=True, null=True)

    def __str__(self):
        return str(self.group_name) + ' ' + str(self.course.course_name) + ' ' + str(self.course.faculty)

    class Meta:
        ordering = ('group_name',)
        verbose_name = 'Группа'
        verbose_name_plural = '3. Группы'


class EmployeeCadet(models.Model):
    group_fk = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.SET_NULL, blank=True,
                                 null=True)
    last_name = models.CharField(verbose_name="Фамилия", max_length=255)
    first_name = models.CharField(verbose_name="Имя", max_length=255, blank=True, null=True)
    patronymic = models.CharField(verbose_name="Отчество", max_length=255, blank=True, null=True)

    date_of_birth = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    year_of_entering = models.IntegerField(verbose_name="Год поступления", blank=True, null=True)

    covid_1_date = models.DateField(verbose_name="Дата первой прививки", blank=True, null=True)
    covid_2_date = models.DateField(verbose_name="Дата второй прививки", blank=True, null=True)
    is_willing = models.BooleanField(verbose_name="Желает пройти вакцинацию", default=False)
    last_modified = models.DateTimeField(verbose_name="Дата и время последнего редактирования", auto_now=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.patronymic

    class Meta:
        ordering = ('last_name',)
        verbose_name = 'Курсант'
        verbose_name_plural = '4. Курсанты'