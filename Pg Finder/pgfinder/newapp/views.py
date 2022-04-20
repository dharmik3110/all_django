from django.http import HttpResponse
from django.shortcuts import render

import newapp
from .models import Student
import email

# Create your views here.

def addStudent(request):
    std = Student(name = 'dharmik', age = 22, email = 'dharmik@gmail.com')
    #std = Student(name = 'dharmik', age = 22, email = 'dharmik@gmail.com')
    
    std.save()
    return HttpResponse("student added..")

def viewStudent(request):
    vsd = Student.objects.all().values_list()
    # print(vsd[0])
    newlist=[]
    # a = list()
    for i in vsd[0]:
        newlist.append(i)
        # print("new list ",newlist)

    context = {
        'vsd': newlist
    }
    return render(request,'newapp/Student.html',context)

def delStudent(request):
    delStudent = Student.objects.get(id=1)
    delStudent.delete()
    
    return HttpResponse("student deletd..")

def updateStudent(request):
    upStudent = Student.objects.get(id=6)
    upStudent.name = 'viraj'
    upStudent.save()
    
    return HttpResponse("student updated..")





