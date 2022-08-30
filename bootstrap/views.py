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
                messages.success(request, 'Order created successfuly') 

                return redirect('/')  
            except:  
                pass 
    else:  
        form = EmployeeForm()  
        
    return render(request,'index.html',{'form':form})  

def index(request):  
    employees = Employee.objects.all()  
    return render(request,"show.html",{'employees':employees})  

def edit(request, id):  
    employee = Employee.objects.get(id=id)  
    return render(request,'edit.html', {'employee':employee})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)  
    if form.is_valid():  
        form.save()  
        messages.success(request, 'Order updated successfuly') 
        return redirect("/") 

    return render(request, 'edit.html', {'employee': employee})  

def destroy(request, id):  
    employee = Employee.objects.get(id=id)  
    employee.delete()  
    messages.success(request, 'Order deleted successfuly') 

    return redirect("/")  

def deleted(request):  
    if request.method == 'POST':
        employees = request.POST.getlist('employees')
        for employ in employees:
            # print(employ)
            employ = Employee.objects.get(pk=employ)
            employ.delete()  
    messages.success(request, 'Order deleted successfuly') 

    return redirect("/")  

def ajaxdelete(request):
    # return redirect (request, "/")
    return render (request, 'ajaxdelete.html')

def responsive(request):  
    return render(request,"responsive.html") 