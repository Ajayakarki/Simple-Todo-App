from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task

from .forms import TaskForm,UpdateTaskForm

# Create your views here.

def index(request):     
    todo = Task.objects.all()
    ## Counting the total number of todo list in the page
    all_task_counter = todo.count()

    ## For completed task
    completed_task = Task.objects.filter(complete=True)
    count_completed_task = completed_task.count()

    progress_task = Task.objects.filter(progress=True)
    count_progress_task = progress_task.count()

    ## For incompleted task we just do the difference between all the tasks and the completed tasks
    count_incompleted_task = all_task_counter - count_completed_task

    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
      

    else:
        form = TaskForm()

    context = {  ### We have to take key inside ''  <=======
        'todos': todo, ## For displaying all data from the database
        'form': form,  ## Django forms
        'all_task_counter': all_task_counter, ## Counting the total number of task in the list
        'count_completed_task': count_completed_task, ## Counting the completed tasks
        'count_incompleted_task': count_incompleted_task, ## Counting the incmomplete tasks
        'count_progress_task': count_progress_task


    }

    return render(request, 'todotemp/index.html', context)


def update(request, pk):

    ## getting the unique id from the Task model
    todo = Task.objects.get(id=pk)
    
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UpdateTaskForm(instance=todo)
    context = {
        'form':form,
    }
    return render(request, 'todotemp/update.html',context)

def delete(request, pk):

    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
  

    return render(request, 'todotemp/delete.html')

