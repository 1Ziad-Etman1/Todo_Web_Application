from django.shortcuts import render
from django.urls import reverse_lazy
from home.models import Task
from django.views.generic import DetailView,DeleteView,UpdateView

# Create your views here.

def addTask(request):
    context = {'success' : False}
    if request.method =='POST':
        title = request.POST['title']
        desc = request.POST['description']
        ins = Task(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success' : True}
        

    return render(request, 'addTask.html', context)

def tasks(request):
    allTasks = Task.objects.all()
    context = {'tasks' : allTasks}
    return render(request, 'tasks.html', context)



class Edit(UpdateView): 
    model = Task
    template_name = 'edit.html'
    fields = '__all__'
    success_url = reverse_lazy('tasks')


class Delete(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('tasks')


class Details(DetailView):
    model = Task
    template_name = 'details.html'