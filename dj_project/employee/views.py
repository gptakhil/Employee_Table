from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


#CREATE
@csrf_exempt 
def employee_create(request):

  if request.method=="POST":
    form=EmployeeForm(request.POST)
    if form.is_valid():
      try:
        form.save()
        return redirect('/employee')
      except: print("Invalid Form")
  else:
    form=EmployeeForm()
  return render(request,'form.html',{'form':form})

#READ

def employee_read(request):
  employee_list=Employee.objects.all()
  return render(request, 'home.html',{'employees':employee_list})


def employee_edit(request,id):
  employee=Employee.objects.get(id=id)
  return render(request,'update.html',{'employee':employee})

#UPDATE

def employee_update(request, id):
  employee = Employee.objects.get(id=id)

  if request.method=="POST":
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
      form.save()
      return redirect("/employee")

  return render(request, 'update.html', {'employee': employee})


#DELETE

def employee_delete(request,id):
  employee=Employee.objects.get(id=id)
  employee.delete()
  return redirect('/employee')
