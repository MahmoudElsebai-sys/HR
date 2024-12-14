from django.db import models

# Model representing a department
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Department name (unique)
    location = models.CharField(max_length=255, blank=True, null=True)  # Optional department location

    def __str__(self):
        return self.name


# Model representing an employee
class Employee(models.Model):
    JOB_TITLE = [
        ('Manager', 'Manager'),
        ('Head of Department', 'Head of Department'),
        ('Supervisor', 'Supervisor'),
        ('Senior Specialist', 'Senior Specialist'),
        ('Specialist', 'Specialist'),
        ('Coordinator', 'Coordinator'),
    ]
    employee_id = models.AutoField(primary_key=True)  # Unique employee ID
    first_name = models.CharField(max_length=100)  # First name
    last_name = models.CharField(max_length=100)  # Last name
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])  # Gender
    birth_date = models.DateField()  # Date of birth
    phone_number = models.CharField(max_length=15)  # Phone number
    email = models.EmailField(max_length=100)  # Email address
    address = models.CharField(max_length=255)  # Home address
    hire_date = models.DateField()  # Date of hiring
    status = models.CharField(max_length=50, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])  # Employment status
    job_title = models.CharField(max_length=50, choices=JOB_TITLE, null=False, default='Coordinator')  # Job title
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  # Associated department

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name} ({self.department}) - {self.job_title}"


# Model representing employee attendance
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Related employee
    date = models.DateField()  # Attendance date
    check_in = models.TimeField(null=True, blank=True)  # Check-in time
    check_out = models.TimeField(null=True, blank=True)  # Check-out time

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.employee.department} - {self.date}"


# Model representing employee salary details
class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Associated employee
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)  # Basic salary
    allowances = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Allowances (optional)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Deductions (optional)

    def __str__(self):
        return f"Salary for {self.employee.first_name}"


# Model representing employee leave details
class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('annual', 'Annual Leave'),  # Annual leave
        ('sick', 'Sick Leave'),      # Sick leave
        ('maternity', 'Maternity Leave'),  # Maternity leave
        ('paternity', 'Paternity Leave'),  # Paternity leave
        ('unpaid', 'Unpaid Leave'),  # Unpaid leave
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Associated employee
    start_date = models.DateTimeField(null=False)  # Start date of leave
    end_date = models.DateTimeField(null=False)  # End date of leave
    leave_type = models.CharField(max_length=20, default='annual', choices=LEAVE_TYPE_CHOICES)  # Type of leave
    reason = models.TextField(null=True, blank=True)  # Reason for leave (optional)

    def __str__(self):
        return f"{self.employee.first_name} {self.employee.last_name} - {self.leave_type}"


# Uncomment this section to include performance reviews
# class PerformanceReview(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE)  # Related employee
#     review_date = models.DateField()  # Date of the review
#     reviewer = models.CharField(max_length=100)  # Reviewer name
#     score = models.IntegerField()  # Performance score (e.g., 1 to 10)
#     comments = models.TextField(null=True, blank=True)  # Review comments

#     def __str__(self):
#         return f"Review for {self.employee.first_name} on {self.review_date}"
