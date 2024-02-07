from django.shortcuts import render, redirect
from .models import Task

# Create your views here.

def index(request):
    object_list = Task.objects.all()
    return render(request,'index.html', {'object_list': object_list})

def addtask(request):
    return render(request, 'addtask.html')

def addtolist(request):
    a = request.POST['first']
    b = request.POST['second']
    c = request.POST['third']
    value = Task(title=a,description=b,due_date=c)
    value.save()
    return redirect('/')

def updpage(request,id):
    val = Task.objects.get(id=id)
    return render(request, 'update.html',{'val':val})

def updatelist(request,id):
    x = request.POST['first']
    y = request.POST['second']
    z = request.POST['third']
    val1 = Task.objects.get(id=id)
    val1.title = x
    val1.description = y
    val1.due_date = z
    val1.save()
    return redirect('/')

def dellist(request,id):
    val2 = Task.objects.get(id=id)
    val2.delete()
    return redirect('/')



