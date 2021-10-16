# Generated by Django 3.2.8 on 2021-10-16 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subdivision_name', models.CharField(max_length=255, verbose_name='Подразделение')),
                ('subdivision_short_name', models.CharField(max_length=255, verbose_name='Короткое название подразделения (только заглавные английские буквы)')),
                ('last_modified', models.DateTimeField(blank=True, null=True, verbose_name='Дата и время последнего редактирования')),
            ],
            options={
                'verbose_name': 'Подразделение',
                'verbose_name_plural': 'Подразделения',
                'ordering': ('subdivision_name',),
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255, verbose_name='Фамилия')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=255, null=True, verbose_name='Отчество')),
                ('covid_1_date', models.DateField(blank=True, null=True, verbose_name='Дата первой прививки')),
                ('covid_2_date', models.DateField(blank=True, null=True, verbose_name='Дата второй прививки')),
                ('is_willing', models.BooleanField(default=False, verbose_name='Желает пройти вакцинацию')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Дата и время последнего редактирования')),
                ('is_fired', models.BooleanField(default=False, verbose_name='Уволен')),
                ('subdivision', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='covid_old.subdivision', verbose_name='Подразделение')),
            ],
            options={
                'verbose_name': 'Сотрудник',
                'verbose_name_plural': 'Сотрудники',
                'ordering': ('last_name',),
            },
        ),
    ]
