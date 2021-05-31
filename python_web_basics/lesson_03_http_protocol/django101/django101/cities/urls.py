# cities.urls

from django.urls import path
from django.views.generic import TemplateView

from django101.cities.views import index, list_phones, test_index, create_person

urlpatterns = [
    path('', index),    # localhost:8000 +  cities / + ''
    path('create/', create_person),
    path('test/', test_index),
    path('phones/', list_phones),    # localhost:8000 + cities/ + phones/
    path('phones2/', TemplateView.as_view(template_name='cities/phones.html')),
]
