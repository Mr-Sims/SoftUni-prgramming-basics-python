from articles.web.views import ArticlesListView, ArticleCreateView, SourceCreateView, SourcesListView, SourceDetailView

from django.urls import path

urlpatterns = [
    path('', ArticlesListView.as_view(), name='index'),
    path('articles/create/', ArticleCreateView.as_view(), name='create article'),
    path('sources/', SourcesListView.as_view(), name='list sources'),
    path('sources/create/', SourceCreateView.as_view(), name='create source'),
    path('sources/<int:pk>', SourceDetailView.as_view(), name='detail source')
]
