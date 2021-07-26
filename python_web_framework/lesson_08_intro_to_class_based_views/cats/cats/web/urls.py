from django.urls import path

from cats.web.views import show_cats, index, IndexView, ShowCatsListsView, CatCreateView

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexView.as_view(), name='cbv index'),

    path('cats/', show_cats, name='show cats'),
    path('cats-cbv/', ShowCatsListsView.as_view(), name='cbv cats list'),
    path('create/', CatCreateView.as_view(), name='create cat'),
)
