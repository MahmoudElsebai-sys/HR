# Generated by Django 5.1.4 on 2024-12-13 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('birth_date', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('hire_date', models.DateField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('job_title', models.CharField(choices=[('Manager', 'Manager'), ('Head of Department', 'Head of Department'), ('Supervisor', 'Supervisor'), ('Senior Specialist', 'Senior Specialist'), ('Specialist', 'Specialist'), ('Coordinator', 'Coordinator')], default='Coordinator', max_length=50)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HR.department')),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in', models.TimeField(blank=True, null=True)),
                ('check_out', models.TimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('leave_type', models.CharField(choices=[('annual', 'Annual Leave'), ('sick', 'Sick Leave'), ('maternity', 'Maternity Leave'), ('paternity', 'Paternity Leave'), ('unpaid', 'Unpaid Leave')], default='annual', max_length=20)),
                ('reason', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HR.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('allowances', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('deductions', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HR.employee')),
            ],
        ),
    ]
