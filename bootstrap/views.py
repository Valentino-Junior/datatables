#views.py
from django.shortcuts import render, redirect  
from .forms import EmployeeForm  
from .models import Employee 

from django.contrib import messages


# Create your views here.  
def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/')  
            except:  
                pass 
    else:  
        form = EmployeeForm()  

    messages.success(request, 'Order updated successfuly') 

    return render(request,'index.html',{'form':form})  
def index(request):  
    employees = Employee.objects.all()  
    messages.success(request, 'Order updated successfuly') 

    return render(request,"show.html",{'employees':employees})  
def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  
def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        return redirect("/")     
    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    return redirect("/")  


def responsive(request):  
    return render(request,"responsive.html") 