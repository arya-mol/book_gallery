from django.db import models

# Create your models here.

class Employees(models.Model):
    employee_name=models.CharField(max_length=120)
    department=models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    salary=models.PositiveIntegerField()
    experience=models.PositiveIntegerField()
    active_status=models.BooleanField(default=True)

    def __str__(self):
        return self.employee_name

#ORM queries for creating new employee
# emp=Employees(emp_name="abc",department="dev",email="abc@gmail.com",salary=30000,experience=5)
#emp.save()

#ORM queries for listing all employees
#employees=Employees.objects.all()
#employees

#ORM queries for filtering employees
#print all employees whoes department=HR
# employees=Employees.objects.filter(department="HR")

#print all details
#for emp in employees:
#   print(emp.employee_name,emp.department,emp.email,emp.salary,emp.experience)

#print all employees whoes experience>5
# employees=Employees.objects.filter(experience__gt=5)
# employees

#print all employees whoes salary>35000
# employees=Employees.objects.filter(salary__gt=35000)
# employees

#print all employees whoes salary<35000
# employees=Employees.objects.filter(salary__lt=35000)
# employees

#print all employees whoes salary>=30000
# employees=Employees.objects.filter(salary__gte=30000)
# employees

#print all employees whoes salary<=30000
# employees=Employees.objects.filter(salary__lte=30000)
# employees

# print all employees whoes experience in range of 5 to 8
# employees=Employees.objects.filter(experience__gt=5,experience__lt=8)
# employees

# print a specific object
# ORM query for fetching Arya record
#employee=Employees.objects.get(id=1)