from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, ListView, UpdateView, DeleteView

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.core.forms import BootstrapFormViewMixin
from petstagram.pets.forms import PetForm, EditPetForm
from petstagram.pets.models import Pet, Like


def list_pets(request):
    # all_pets = sorted(Pet.objects.all(), key=id, reverse=True)
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets,
    }
    return render(request, 'pet_list.html', context)


class ListPetsView(ListView):
    template_name = 'pet_list.html'
    context_object_name = 'pets'
    model = Pet


class PetDetailsView(DetailView):
    model = Pet
    template_name = 'pet_detail.html'
    context_object_name = 'pet'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pet = context['pet']

        pet.likes_count = pet.like_set.count()
        is_owner = pet.user == self.request.user

        is_liked_by_user = pet.like_set.filter(user_id=self.request.user.id).exists()

        context['comment_form'] = CommentForm(
                initial={
                    'pet_pk': self.object.id,
                }
            )
        context['comments'] = pet.comment_set.all()
        context['is_owner'] = is_owner
        context['is_liked'] = is_liked_by_user

        return context


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet.likes_count = pet.like_set.count()

    is_owner = pet.user == request.user

    is_liked_by_user = pet.like_set.filter(user_id=request.user.id).exists()

    context = {
        'pet': pet,
        'comment_form': CommentForm(
            initial={
                'pet_pk': pk,
            }
        ),
        'comments': pet.comment_set.all(),
        'is_owner': is_owner,
        'is_liked': is_liked_by_user,
    }
    return render(request, 'pet_detail.html', context)


###########################
# # V1 COMMENT_PET - standard form
###########################
# def comment_pet(request, pk):
#     pet = Pet.objects.get(pk=pk)
#     form = CommentForm(request.POST)
#     if form.is_valid():
#         comment = Comment(
#             comment=form.cleaned_data['text'],
#             pet=pet
#         )
#         comment.save()
#     return redirect('pet details', pet.id)

#################################
# # V2 FOR COMMENT PET - model form
#################################
@login_required()
def comment_pet(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
    return redirect('pet details', pk)


class PostOnlyView(View):
    form_class = None

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass


class CommentPetView(LoginRequiredMixin, PostOnlyView):
    form_class = CommentForm

    def form_valid(self, form):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet=pet,
            user=self.request.user,
        )
        comment.save()
        return redirect('pet details', pet.id)

    def form_invalid(self, form):
        pass


class LikePetView(LoginRequiredMixin, PostOnlyView):
    #
    # def get(self, request, *args, **kwargs):
    #     pet = Pet.objects.get(pk=self.kwargs['pk'])
    #     return redirect('pet details', pet.id)

    def post(self, request, *args, **kwargs):
        pet = Pet.objects.get(pk=self.kwargs['pk'])
        like_object_by_user = pet.like_set.filter(user_id=self.request.user.id).first()
        if like_object_by_user:
            like_object_by_user.delete()
        else:
            like = Like(
                pet=pet,
                user=self.request.user,
            )
            like.save()
        return redirect('pet details', pet.id)

@login_required()
def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like_object_by_user = pet.like_set.filter(user_id=request.user.id).first()
    if like_object_by_user:
        like_object_by_user.delete()
    else:
        like = Like(
            pet=pet,
            user=request.user,
        )
        like.save()
    return redirect('pet details', pet.id)


class CreatePetView(LoginRequiredMixin, BootstrapFormViewMixin, CreateView):
    template_name = 'pet_create.html'
    model = Pet
    fields = ('type', 'name', 'age', 'description', 'image')
    # form_class = PetForm
    success_url = reverse_lazy('list pets')

    def form_valid(self, form):
        pet = form.save(commit=False)
        pet.user = self.request.user
        pet.save()
        return super().form_valid(form)


@login_required
def create_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')
    else:
        form = PetForm()
    context = {
        'form': form,
    }
    return render(request, 'pet_create.html', context)


class EditPetView(LoginRequiredMixin, BootstrapFormViewMixin, UpdateView):
    model = Pet
    form_class = EditPetForm
    template_name = 'pet_edit.html'
    success_url = reverse_lazy('list pets')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        form = EditPetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    else:
        form = EditPetForm(instance=pet)
    context = {
        'form': form,
        'pet': pet
    }
    return render(request, 'pet_edit.html', context)


class DeletePetView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pet_delete.html'
    success_url = reverse_lazy('list pets')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('list pets')
    else:
        context = {
            'pet': pet
        }
        return render(request, 'pet_delete.html', context)
