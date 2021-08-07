from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, DeleteView, CreateView, UpdateView

from notes.main_content.forms import CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes.main_content.models import Note

UserModel = get_user_model()


def home(request):
    user = UserModel(pk=request.user.id)
    notes_by_user = Note.objects.filter(user_id=request.user.id)
    context = {
        'notes': notes_by_user,
        'user': user
    }
    return render(request, 'profile/index.html', context)

# @login_required
# def create_note(request):
#     if request.method == "POST":
#         form = CreateNoteForm(request.POST, request.FILES)
#         if form.is_valid():
#             note = form.save(commit=False)
#             note.user = request.user
#             note.save()
#             return redirect('home')
#     else:
#         form = CreateNoteForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'notes/note-create.html', context)

#Class-Based-View
class NoteCreateView(CreateView):
    # form_class = CreateNoteForm
    fields = ('title', 'content', 'image')
    model = Note
    template_name = 'notes/note-create.html'
    success_url = reverse_lazy('home')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(NoteCreateView, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)


# @login_required
# def edit_note(request, pk):
#     note = Note.objects.get(pk=pk)
#     if request.method == "POST":
#         form = EditNoteForm(request.POST, request.FILES, instance=note)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = EditNoteForm(instance=note)
#     context = {
#         'note': note,
#         'form': form
#     }
#     return render(request, 'notes/note-edit.html', context)


class NoteUpdateView(UpdateView):
    form_class = EditNoteForm
    model = Note
    template_name = 'notes/note-edit.html'
    success_url = reverse_lazy('home')


@login_required
def delete_note(request, pk):
    note = Note.objects.get(pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect('home')
    else:
        form = DeleteNoteForm(instance=note)
    context = {
        'note': note,
        'form': form
    }
    return render(request, 'notes/note-delete.html', context)


#Class-Based_View
# class NoteDeleteView(DeleteView):
#     fields = '__all__'
#     model = Note
#     template_name = 'notes/note-delete.html'
#     context_object_name = 'note'
#     success_url = reverse_lazy('home')


#Function-Based-View
# @login_required
# def note_details(request, pk):
#     note = Note.objects.get(pk=pk)
#     context = {
#         'note': note
#     }
#     return render(request, 'notes/note-details.html', context)


#Class-Based_View
class NoteDetailView(DetailView):
    template_name = 'notes/note-details.html'
    context_object_name = 'note'
    model = Note


