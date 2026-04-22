from django.shortcuts import render
from .models import Task
from .forms import Taskform
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(login_url='/admin/')
def list_create_view(request):
    if request.method == "POST":
        form = Taskform(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            context = {'data': task}
            return render(request, 'home/task-list.html', context)

    task_list = Task.objects.filter(user=request.user).all().order_by('-date_created')
    context = {'data': task_list, 'form': Taskform()}
    return render(request, 'home/task-list.html', context)
