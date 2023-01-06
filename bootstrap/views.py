#views.py
from django.shortcuts import render, redirect  
from .forms import * 
from .models import Employee 

from django.contrib import messages
from django.http import HttpResponse



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
    messages.success(request, 'Order delete successfuly') 

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

def flowbite(request):
    # return redirect (request, "/")
    return render (request, 'flowbite.html')

def responsive(request):  
    return render(request,"responsive.html") 

def modal_datatable(request):  
    return render(request,"modal datatable.html") 

def tailwind(request):
    contetxt= {}
    return render (request, 'tailwind.html')



# def file_upload_view(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # handle the uploaded files and instructions
#             files = request.FILES.getlist('files')
#             instructions = request.POST['instructions']
#             for f in files:
#                  file_instance = Photo(files=f)
#                  file_instance.save()
#                 # do something with the file, such as saving it to the database or storing it on the filesystem
#             pass
#             instruct = Photo(instructions = instructions)
#             instruct.save()

#             # do something with the instructions, such as saving them to the database or processing them
#             pass
#     else:
#         form = FileUploadForm()
#     return render(request, 'upload.html', {'form': form})



def upload_files(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST)
        if form.is_valid():
            # Save the instructions to the database
            # instructions = form.cleaned_data['instructions']
            # FileModel.objects.create(instructions=instructions)

            # Save the uploaded files to the database
            for file in request.FILES.getlist('file'):
                FileModel.objects.create(files=file)

            # return redirect('success')
    else:
        form = FileUploadForm()

        # return HttpResponse()
    return render(request, 'upload.html', {'form': form})