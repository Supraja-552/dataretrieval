from django.shortcuts import render
from app.models import *
# Create your views here.
def dept(request):
    QLDO=Department.objects.all()
    d={
        'QLDO':QLDO}
    return render(request,'dept.html',d)
def emp(request):
    QLEO=Employee.objects.all()
    d={'QLEO':QLEO}
    return render(request,'emp.html',d)