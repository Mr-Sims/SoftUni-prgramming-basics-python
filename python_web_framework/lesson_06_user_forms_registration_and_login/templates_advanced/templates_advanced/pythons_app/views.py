from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .forms import PythonCreateForm
from .models import Python


# def test_view(request):
#     user = authenticate(username='simo', password='maznaparola')
#     login(request, user)
#     return redirect('index')
from ..core.decorators import any_group_required


def index(request):
    user = request.user
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


#@login_required(login_url=reverse_lazy('sign in'))
@any_group_required(groups=['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'create.html', {'form':form})