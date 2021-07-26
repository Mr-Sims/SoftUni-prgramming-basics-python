from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from cats.common.form_mixins import BootStrapFormViewMixin
from cats.web.models import Cat


def index(request):
    context = {
        'title': 'Hello this is a Func-Based View'
    }
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Hello this is a Class-Based View'
        }

#########################################################


def show_cats(request):
    context = {
        'cats': Cat.objects.all(),
        'cats_title': 'Hello func based cats',
    }
    return render(request, 'cats.html', context)


class CatCreateView(BootStrapFormViewMixin, CreateView):
    model = Cat
    fields = '__all__'
    template_name = 'create-cat.html'
    success_url = reverse_lazy('cbv cats list')





class ShowCatsListsView(ListView):
    model = Cat
    template_name = 'cats.html'
    context_object_name = 'cats'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cats_title'] = 'Hello CLASS based cats'
        return context