from django.http import HttpResponse
from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        "name": "Simo",
        "people": Person.objects.all()

    }
    return render(req, 'index.html', context)


def list_phones(request):
    context = {
        'phones': [
            {
                'name': "GalaxyS500",
                'quantity': 3
            },
            {
                'name': 'Xiaoiu',
                'quantity': 0
            },
            {
                'name': 'iPhone18',
                'quantity': 4
            }
        ]
        # 'phones': []
    }
    context['message'] = "Phones List"
    return render(request, 'phones.html', context)