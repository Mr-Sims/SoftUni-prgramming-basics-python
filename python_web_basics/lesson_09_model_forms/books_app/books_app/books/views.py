from django.shortcuts import render, redirect

from books_app.books.forms import BookForm
from books_app.books.models import Book


def index(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'index.html', context)


def create_book(request):
    if request.method == "GET":
        context = {
            'form': BookForm() ,
        }
        return render(request, 'create.html', context)

    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'create.html', context)


def update_book(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == "GET":
        context = {
            'form': BookForm(initial=book.__dict__),
        }
        return render(request, 'edit.html', context)
    else:
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
        context = {
            'form': form
        }
        return render(request, 'edit.html', context)