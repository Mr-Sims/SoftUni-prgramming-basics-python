from django.shortcuts import render, redirect

from templates_advanced_demo.todos.forms import TodoForm
from templates_advanced_demo.todos.models import Todo


def list_todos(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
        'page_name': 'list_todos'
    }
    return render(request, 'list_todos.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list todos')
    else:
        form = TodoForm()

    context = {
        'form':form,
        'page_name': 'create_todos'
    }
    return render(request, 'create_todo.html', context)