from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Task
from .forms import Taskform
from django.contrib.auth.decorators import login_required


@login_required(login_url='/admin/')
def task_list_view(request):
    task_list = Task.objects.filter(user=request.user).all().order_by('-date_created')
    context = {'all_tasks': task_list}
    return render(request, 'home/task-list.html', context)


@login_required(login_url='/admin/')
def task_create_view(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            context = {'task': task }
            return render(request, 'home/task-row.html', context)
        
    context = {
        'form': Taskform(),
        'action_url': '/create/',
        'swap_type': 'afterbegin'
        }
    return render(request, 'home/task-form.html', context)

@login_required(login_url='/admin/')  
def task_update(request, id):
    task = get_object_or_404(Task, user = request.user, id=id)
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task_item = form.save(commit=False)
            task_item.user = request.user
            task_item.save()
            context = {'task': task_item}
            return render(request, 'home/task-row.html', context)
    else:
        context = {
            'form': Taskform(instance = task),
            'action_url': f"/update/{id}/",
            'swap_type': 'outerHTML',
        }
        return render(request, 'home/task-form.html', context)


@login_required(login_url='/admin/')  
def tasK_delete(request, id):
    task = get_object_or_404(Task, user=request.user, id=id)
    task.delete()
    return HttpResponse('')