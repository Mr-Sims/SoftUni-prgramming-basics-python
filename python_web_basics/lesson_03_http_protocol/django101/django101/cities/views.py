from django.http import HttpResponse
from django.shortcuts import render, redirect

from django101.cities.models import Person


def index(request):
    context = {
        'name': 'Simo',
        'people': Person.objects.all(),
    }
    return render(request, 'index.html', context)


def create_person(request):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia'
    ).save()

    return redirect('/cities')


def test_index(request):
    return HttpResponse(
        '{"name": "Simo"}',
        content_type='application/json')


def list_phones(request):
    context = {
        'phones':[
            {
                'name':'Galaxy S500',
                'quantity': 3
            },
            {
                'name': 'Xiaomi RedMi',
                'quantity': 0
            },
            {
                'name': 'iPhone 12',
                'quantity': 3
            }
        ]
    }
    context['message'] = 'Phones List'
    return render(request, "cities/phones.html", context)
