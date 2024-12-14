from django.shortcuts import render ,HttpResponse
from.models import Employee ,Department

def index(request):
    return render(request,'index.html')

def employee_list (request):
    employee=Employee.objects.all()
    return render(request,'employee/employee.html',{'employee':employee})


def department(reqeste):
    department=Department.objects.all()# display all objects in department
    return render(reqeste,'department/department.html',{'department':department})

# Create your views here.
