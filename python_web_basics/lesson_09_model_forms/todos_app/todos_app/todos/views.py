from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm, CreateTodoForm2
from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


# # This below should work with the original index.html that we already created in the last lesson and developed today.
# def index(request):
#     todos = Todo.objects.all()
#     context = {
#         'todos': todos,
#         'form': CreateTodoForm(),
#     }
#
#     return render(request, 'index.html', context=context)
#
#
# def create_todo(request):
#     form = CreateTodoForm(request.POST)
#
#     if form.is_valid():
#         # cleaned_data is available only after is_valid() call
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             #owner=owner,
#         )
#         todo.save()
#         return redirect('/'
#     else:
#         context = {
#             'todos': Todo.objects.all(),
#             'form': form,
#         }
#         return render(request, 'index.html', context)
#
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')

##This below should work with the new html files given to us by good guys softuni crew

def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'index_1.html', context)


def create_todo(request):
    form = CreateTodoForm2(request.POST)

    if request.method == "POST":
        if form.is_valid():
            todo = Todo(
                text=form.cleaned_data['text'],
                description=form.cleaned_data['description'],
                state=False,
            )
            todo.save()
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    todo = Todo.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'form': CreateTodoForm2(initial=todo.__dict__),
        }
        return render(request, 'edit.html', context)
    else:
        form = CreateTodoForm2(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    return redirect('/')

