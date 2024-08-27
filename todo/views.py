from django.shortcuts import render, redirect, get_object_or_404
from .models import todo
from .form import TodoForm

def home(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(todo_name=task)
        new_todo.save()

    all_todos = todo.objects.all()
    context = {
        'todos': all_todos
    }
    return render(request, 'todoapp/todo.html', context)

def DeleteTask(request, id):
    get_todo = get_object_or_404(todo, id=id)
    get_todo.delete()
    return redirect('home-page')

def Update(request, id):
    get_todo = get_object_or_404(todo, id=id)
    get_todo.status = True
    get_todo.save()
    return redirect('home-page')

def EditTask(request, id):

    get_todo = get_object_or_404(todo, id=id)
    form = TodoForm(instance=get_todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=get_todo)
        if form.is_valid():
            form.save()
            return redirect('home-page')
   
    context={
        'the_form': form
    }
    return render(request=request, template_name="todoapp/edit_task.html", context=context)