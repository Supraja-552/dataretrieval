from django.db import models

# Create your models here.
class Department(models.Model):
    Dept_no=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)
    no_of_employee=models.IntegerField()
    dept_url=models.URLField(default='https://django.in')
    def __str__(self):
        return self.Dname
    
class Employee(models.Model):
    Emp_no=models.IntegerField()
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Mgr=models.IntegerField()
    Hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True)
    Dept_no=models.OneToOneField(Department,on_delete=models.CASCADE)
    def __str__(self):
        return self.Ename
class SalGrade(models.Model):
    Grade=models.IntegerField()
    Losal=models.IntegerField()
    Hisal=models.IntegerField()
class Bonus(models.Model):
    Ename=models.CharField(max_length=100)
    Job=models.CharField(max_length=100)
    Salary=models.IntegerField()
    comm=models.IntegerField()
