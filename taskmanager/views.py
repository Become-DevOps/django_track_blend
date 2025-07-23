from django.shortcuts import render,redirect
from taskmanager.models import Tasks
from taskmanager.forms import taskForm,editForm
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = taskForm(request.POST)
        
        if form.is_valid():
            form.save()
         
    form = taskForm()   
    alltasks = Tasks.objects.all()
    paginator = Paginator(alltasks,4)
    page = request.GET.get('pg')
    alltasks = paginator.get_page(page)
    return render(request,"tasks/index.html",{'alltasks':alltasks,'form':form})

def editTask(request,id):
    if request.method == 'POST':
        res = Tasks.objects.get(id=id)
        form = editForm(request.POST,instance=res)
        if form.is_valid():
            form.save()
            return redirect("taskmanager:task")
        
    res = Tasks.objects.get(id=id)
    form = editForm(instance=res)
    return render(request,"tasks/edittask.html",{'form':form})

def deletetask(request,id):
    res = Tasks.objects.get(id=id)
    res.delete()
    return redirect("taskmanager:task")